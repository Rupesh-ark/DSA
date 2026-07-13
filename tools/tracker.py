#!/usr/bin/env python3

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "data" / "neetcode150.csv"
PROGRESS_PATH = ROOT / "data" / "progress.json"
REVIEW_INTERVALS = (1, 7, 21)
SESSION_FIELDS = {
    "date",
    "problem",
    "kind",
    "outcome",
    "minutes",
    "tests_passed",
    "complexity_explained",
    "takeaway",
}
KINDS = ("new", "review")
OUTCOMES = ("attempted", "helped", "independent")


@dataclass(frozen=True)
class Problem:
    slug: str
    title: str
    category: str
    difficulty: str
    url: str


@dataclass(frozen=True)
class Review:
    problem: Problem
    due_on: date
    independent_successes: int

    @property
    def label(self) -> str:
        labels = {
            0: "independent retry",
            1: "1-day recall",
            2: "7-day implementation",
            3: "21-day full solve",
        }
        return labels[self.independent_successes]


def parse_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"Invalid ISO date: {value}") from error


def load_catalog(path: Path = CATALOG_PATH) -> list[Problem]:
    required = {"slug", "title", "category", "difficulty", "url"}
    with path.open(newline="", encoding="utf-8") as catalogue_file:
        reader = csv.DictReader(catalogue_file)
        if set(reader.fieldnames or ()) != required:
            raise ValueError("The catalogue header is invalid.")
        problems = [Problem(**row) for row in reader]

    slugs = [problem.slug for problem in problems]
    if len(problems) != 150:
        raise ValueError(f"Expected 150 catalogue entries, found {len(problems)}.")
    if len(set(slugs)) != len(slugs):
        raise ValueError("The catalogue contains duplicate slugs.")
    if any(problem.difficulty not in {"Easy", "Medium", "Hard"} for problem in problems):
        raise ValueError("The catalogue contains an invalid difficulty.")
    return problems


def validate_progress(progress: Any, catalogue: list[Problem]) -> None:
    if not isinstance(progress, dict) or set(progress) != {"version", "sessions"}:
        raise ValueError("Progress must contain only version and sessions.")
    if progress["version"] != 1 or not isinstance(progress["sessions"], list):
        raise ValueError("Unsupported progress format.")

    valid_slugs = {problem.slug for problem in catalogue}
    seen_problem_dates: set[tuple[str, str]] = set()
    for index, session in enumerate(progress["sessions"], start=1):
        prefix = f"Session {index}"
        if not isinstance(session, dict) or set(session) != SESSION_FIELDS:
            raise ValueError(f"{prefix} has invalid fields.")
        parse_date(session["date"])
        if session["problem"] not in valid_slugs:
            raise ValueError(f"{prefix} refers to an unknown problem.")
        if session["kind"] not in KINDS:
            raise ValueError(f"{prefix} has an invalid kind.")
        if session["outcome"] not in OUTCOMES:
            raise ValueError(f"{prefix} has an invalid outcome.")
        if (
            isinstance(session["minutes"], bool)
            or not isinstance(session["minutes"], int)
            or not 1 <= session["minutes"] <= 180
        ):
            raise ValueError(f"{prefix} minutes must be between 1 and 180.")
        if not isinstance(session["tests_passed"], bool):
            raise ValueError(f"{prefix} tests_passed must be true or false.")
        if not isinstance(session["complexity_explained"], bool):
            raise ValueError(f"{prefix} complexity_explained must be true or false.")
        if not isinstance(session["takeaway"], str):
            raise ValueError(f"{prefix} takeaway must be text.")

        problem_date = (session["problem"], session["date"])
        if problem_date in seen_problem_dates:
            raise ValueError(f"{prefix} duplicates a problem already logged that day.")
        seen_problem_dates.add(problem_date)


def load_progress(
    catalogue: list[Problem], path: Path = PROGRESS_PATH
) -> dict[str, Any]:
    try:
        progress = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"Progress is not valid JSON: {error.msg}.") from error
    validate_progress(progress, catalogue)
    return progress


def save_progress(progress: dict[str, Any], path: Path = PROGRESS_PATH) -> None:
    temporary_path = path.with_suffix(".tmp")
    temporary_path.write_text(json.dumps(progress, indent=2) + "\n", encoding="utf-8")
    temporary_path.replace(path)


def sessions_for(slug: str, sessions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        (session for session in sessions if session["problem"] == slug),
        key=lambda session: session["date"],
    )


def independent_successes(slug: str, sessions: list[dict[str, Any]]) -> int:
    return sum(
        session["outcome"] == "independent"
        for session in sessions_for(slug, sessions)
    )


def next_review_date(slug: str, sessions: list[dict[str, Any]]) -> date | None:
    history = sessions_for(slug, sessions)
    if not history:
        return None

    successes = independent_successes(slug, sessions)
    if successes >= 4:
        return None

    latest = history[-1]
    latest_date = parse_date(latest["date"])
    if latest["outcome"] != "independent" or successes == 0:
        return latest_date + timedelta(days=1)
    return latest_date + timedelta(days=REVIEW_INTERVALS[successes - 1])


def due_reviews(
    catalogue: list[Problem], sessions: list[dict[str, Any]], today: date
) -> list[Review]:
    reviews = []
    for problem in catalogue:
        due_on = next_review_date(problem.slug, sessions)
        if due_on is not None and due_on <= today:
            reviews.append(
                Review(problem, due_on, independent_successes(problem.slug, sessions))
            )
    return sorted(reviews, key=lambda review: (review.due_on, review.problem.title))


def next_new_problem(
    catalogue: list[Problem], sessions: list[dict[str, Any]]
) -> Problem | None:
    started = {session["problem"] for session in sessions}
    return next((problem for problem in catalogue if problem.slug not in started), None)


def boss_problem(
    catalogue: list[Problem], sessions: list[dict[str, Any]]
) -> Problem | None:
    practised = []
    by_slug = {problem.slug: problem for problem in catalogue}
    for slug in {session["problem"] for session in sessions}:
        history = sessions_for(slug, sessions)
        practised.append((history[-1]["date"], by_slug[slug]))
    if practised:
        return min(practised, key=lambda item: item[0])[1]
    return next_new_problem(catalogue, sessions)


def calculate_xp(sessions: list[dict[str, Any]]) -> int:
    xp = 10 * len({session["date"] for session in sessions})
    for session in sessions:
        xp += 20
        if session["tests_passed"]:
            xp += 20
        if session["complexity_explained"]:
            xp += 10
        if session["kind"] == "review" and session["outcome"] == "independent":
            xp += 20
    return xp


def streaks(sessions: list[dict[str, Any]], today: date) -> tuple[int, int]:
    active_dates = sorted(
        {parse_date(session["date"]) for session in sessions if parse_date(session["date"]) <= today}
    )
    if not active_dates:
        return 0, 0

    active_set = set(active_dates)
    anchor = today if today in active_set else today - timedelta(days=1)
    current = 0
    while anchor in active_set:
        current += 1
        anchor -= timedelta(days=1)

    best = run = 1
    for previous, current_date in zip(active_dates, active_dates[1:]):
        run = run + 1 if current_date == previous + timedelta(days=1) else 1
        best = max(best, run)
    return current, best


def independent_slugs(sessions: list[dict[str, Any]]) -> set[str]:
    return {
        session["problem"]
        for session in sessions
        if session["outcome"] == "independent"
    }


def mastered_slugs(catalogue: list[Problem], sessions: list[dict[str, Any]]) -> set[str]:
    return {
        problem.slug
        for problem in catalogue
        if independent_successes(problem.slug, sessions) >= 4
    }


def progress_bar(completed: int, total: int, width: int = 30) -> str:
    filled = round(width * completed / total) if total else 0
    return "[" + "#" * filled + "-" * (width - filled) + "]"


def reference_date(value: str | None) -> date:
    return parse_date(value) if value else date.today()


def show_today(catalogue: list[Problem], progress: dict[str, Any], today: date) -> None:
    sessions = progress["sessions"]
    active_dates = {session["date"] for session in sessions}
    day_number = len(active_dates) if today.isoformat() in active_dates else len(active_dates) + 1
    current_streak, _ = streaks(sessions, today)
    reviews = due_reviews(catalogue, sessions, today)

    print(f"NEETCODE 150 - DAY {day_number}")
    print(f"{calculate_xp(sessions)} XP | Current streak: {current_streak} day(s)")
    print()
    print("DUE REVIEWS")
    if reviews:
        for review in reviews[:2]:
            print(
                f"- {review.problem.title} ({review.label}, due {review.due_on.isoformat()})"
            )
        if len(reviews) > 2:
            print(f"- {len(reviews) - 2} more in the review backlog")
    else:
        print("- None today")

    print()
    if today.weekday() == 6:
        problem = boss_problem(catalogue, sessions)
        print("SUNDAY BOSS FIGHT")
        if problem:
            print(f"{problem.title} | {problem.difficulty} | {problem.category}")
            print(problem.url)
        print()
        print("90-MINUTE PLAN")
        print("  60 min  Reviews and weak spots")
        print("  20 min  Boss fight explanation or reimplementation")
        print("  10 min  Log takeaways and prepare the next week")
    else:
        problem = next_new_problem(catalogue, sessions)
        print("TODAY'S QUEST")
        if problem:
            print(f"{problem.title} | {problem.difficulty} | {problem.category}")
            print(problem.url)
        else:
            print("All 150 problems have been attempted. Focus on due reviews.")
        print()
        print("90-MINUTE PLAN")
        if reviews:
            print("  20 min  Due reviews")
        else:
            print("  20 min  Examples and Big-O warm-up")
        print("  55 min  New problem")
        print("  15 min  Complexity, takeaway, and progress log")


def show_stats(catalogue: list[Problem], progress: dict[str, Any], today: date) -> None:
    sessions = progress["sessions"]
    solved = independent_slugs(sessions)
    mastered = mastered_slugs(catalogue, sessions)
    current_streak, best_streak = streaks(sessions, today)
    recent_start = today - timedelta(days=6)
    recent_days = {
        parse_date(session["date"])
        for session in sessions
        if recent_start <= parse_date(session["date"]) <= today
    }

    print("NEETCODE 150 PROGRESS")
    print(f"XP: {calculate_xp(sessions)}")
    print(f"Streak: {current_streak} current | {best_streak} best")
    print(f"Consistency: {len(recent_days)}/7 active days")
    print(
        f"{progress_bar(len(solved), len(catalogue))} "
        f"{len(solved)}/{len(catalogue)} independent | {len(mastered)} mastered"
    )
    print()
    print("CATEGORIES")
    totals = Counter(problem.category for problem in catalogue)
    completed = Counter(
        problem.category for problem in catalogue if problem.slug in solved
    )
    for category in totals:
        print(
            f"{category:<30} {progress_bar(completed[category], totals[category], 12)} "
            f"{completed[category]}/{totals[category]}"
        )


def prompt_choice(label: str, choices: tuple[str, ...], default: str) -> str:
    while True:
        answer = input(f"{label} [{' / '.join(choices)}] ({default}): ").strip().lower()
        answer = answer or default
        if answer in choices:
            return answer
        print(f"Choose one of: {', '.join(choices)}.")


def prompt_bool(label: str) -> bool:
    return prompt_choice(label, ("yes", "no"), "no") == "yes"


def prompt_minutes(default: int) -> int:
    while True:
        answer = input(f"Focused minutes ({default}): ").strip()
        try:
            minutes = int(answer) if answer else default
        except ValueError:
            print("Enter a whole number of minutes.")
            continue
        if 1 <= minutes <= 180:
            return minutes
        print("Minutes must be between 1 and 180.")


def log_session(catalogue: list[Problem], progress: dict[str, Any], today: date) -> None:
    sessions = progress["sessions"]
    reviews = due_reviews(catalogue, sessions, today)
    default_kind = "review" if reviews else "new"
    kind = prompt_choice("Session kind", KINDS, default_kind)

    if kind == "review":
        suggested = reviews[0].problem if reviews else boss_problem(catalogue, sessions)
    else:
        suggested = next_new_problem(catalogue, sessions)
    if suggested is None:
        raise ValueError("There is no problem available for that session kind.")

    problem_by_slug = {problem.slug: problem for problem in catalogue}
    while True:
        slug = input(f"Problem slug ({suggested.slug}): ").strip() or suggested.slug
        if slug in problem_by_slug:
            break
        print("That slug is not in data/neetcode150.csv.")

    history = sessions_for(slug, sessions)
    if kind == "new" and history:
        raise ValueError("That problem has already been started; log it as a review.")
    if kind == "review" and not history:
        raise ValueError("That problem has not been started; log it as new.")

    outcome = prompt_choice("Outcome", OUTCOMES, "attempted")
    new_session = {
        "date": today.isoformat(),
        "problem": slug,
        "kind": kind,
        "outcome": outcome,
        "minutes": prompt_minutes(20 if kind == "review" else 55),
        "tests_passed": prompt_bool("Did your tests pass?"),
        "complexity_explained": prompt_bool("Did you explain time and space complexity?"),
        "takeaway": input("One-sentence takeaway (optional): ").strip(),
    }

    before_xp = calculate_xp(sessions)
    updated_progress = {"version": 1, "sessions": [*sessions, new_session]}
    validate_progress(updated_progress, catalogue)
    save_progress(updated_progress)
    earned = calculate_xp(updated_progress["sessions"]) - before_xp
    problem = problem_by_slug[slug]
    print()
    print(f"Recorded {problem.title}. +{earned} XP")
    due_on = next_review_date(slug, updated_progress["sessions"])
    if due_on:
        print(f"Next review: {due_on.isoformat()}")
    else:
        print("Mastered: all scheduled reviews completed independently.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Local NeetCode 150 learning tracker")
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("today", "stats"):
        command_parser = subparsers.add_parser(command)
        command_parser.add_argument(
            "--date", help="Use YYYY-MM-DD instead of today's local date."
        )
    subparsers.add_parser("log")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        catalogue = load_catalog()
        progress = load_progress(catalogue)
        if args.command == "today":
            show_today(catalogue, progress, reference_date(args.date))
        elif args.command == "stats":
            show_stats(catalogue, progress, reference_date(args.date))
        else:
            log_session(catalogue, progress, date.today())
    except (OSError, ValueError) as error:
        print(f"Error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
