import importlib.util
import sys
import tempfile
import unittest
from collections import Counter
from datetime import date
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock


TRACKER_PATH = Path(__file__).resolve().parents[1] / "tools" / "tracker.py"
SPEC = importlib.util.spec_from_file_location("tracker", TRACKER_PATH)
tracker = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = tracker
SPEC.loader.exec_module(tracker)


def session(
    day: str,
    problem: str = "duplicate-integer",
    kind: str = "new",
    outcome: str = "independent",
    tests_passed: bool = True,
    complexity_explained: bool = True,
) -> dict:
    return {
        "date": day,
        "problem": problem,
        "kind": kind,
        "outcome": outcome,
        "minutes": 55,
        "tests_passed": tests_passed,
        "complexity_explained": complexity_explained,
        "takeaway": "Use a set for membership checks.",
    }


class TrackerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalogue = tracker.load_catalog()

    def test_catalogue_matches_neetcode_150_totals(self) -> None:
        self.assertEqual(len(self.catalogue), 150)
        self.assertEqual(
            Counter(problem.difficulty for problem in self.catalogue),
            {"Easy": 28, "Medium": 101, "Hard": 21},
        )
        self.assertEqual(len({problem.category for problem in self.catalogue}), 18)

    def test_next_problem_follows_catalogue_order(self) -> None:
        self.assertEqual(
            tracker.next_new_problem(self.catalogue, []).slug, "duplicate-integer"
        )
        sessions = [session("2026-07-13")]
        self.assertEqual(
            tracker.next_new_problem(self.catalogue, sessions).slug, "is-anagram"
        )

    def test_attempted_or_helped_problem_remains_locked(self) -> None:
        attempted = [
            session("2026-07-13", outcome="attempted", tests_passed=False)
        ]
        helped = [session("2026-07-13", outcome="helped")]
        self.assertEqual(
            tracker.next_new_problem(self.catalogue, attempted).slug,
            "duplicate-integer",
        )
        self.assertEqual(
            tracker.next_new_problem(self.catalogue, helped).slug,
            "duplicate-integer",
        )

    def test_independent_result_requires_passing_tests(self) -> None:
        sessions = [session("2026-07-13", tests_passed=False)]
        self.assertEqual(
            tracker.next_new_problem(self.catalogue, sessions).slug,
            "duplicate-integer",
        )
        self.assertEqual(tracker.independent_successes("duplicate-integer", sessions), 0)

    def test_finish_outcome_comes_from_tests_and_help(self) -> None:
        self.assertEqual(tracker.outcome_for_result(False, "none"), "attempted")
        self.assertEqual(tracker.outcome_for_result(True, "hint"), "helped")
        self.assertEqual(tracker.outcome_for_result(True, "solution"), "helped")
        self.assertEqual(tracker.outcome_for_result(True, "none"), "independent")

    def test_problem_runner_uses_make_exit_code(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "exercises" / "neetcode150" / "duplicate-integer.cpp"
            source.parent.mkdir(parents=True)
            source.write_text("int main() {}\n", encoding="utf-8")

            passing_runner = Mock(return_value=SimpleNamespace(returncode=0))
            failing_runner = Mock(return_value=SimpleNamespace(returncode=1))
            self.assertTrue(
                tracker.run_problem_tests(
                    "duplicate-integer", root=root, runner=passing_runner
                )
            )
            self.assertFalse(
                tracker.run_problem_tests(
                    "duplicate-integer", root=root, runner=failing_runner
                )
            )
            passing_runner.assert_called_once_with(
                [
                    "make",
                    "--no-print-directory",
                    "run",
                    "EXERCISE=neetcode150/duplicate-integer",
                ],
                cwd=root,
                check=False,
            )

    def test_weekly_challenge_pack_is_local(self) -> None:
        for problem in self.catalogue[:6]:
            with self.subTest(problem=problem.slug):
                challenge = tracker.challenge_text(problem)
                self.assertIsNotNone(challenge)
                self.assertIn("## Challenge", challenge)
                self.assertIn("## Examples", challenge)
                self.assertIn("## Warm-up", challenge)
                self.assertIn("## Function contract", challenge)
                self.assertIn("## Build", challenge)
                self.assertIn(
                    f"exercises/neetcode150/{problem.slug}.cpp", challenge
                )
                self.assertIn(f"make finish PROBLEM={problem.slug}", challenge)
                self.assertIn(problem.url, challenge)
                harness = (
                    tracker.ROOT
                    / "tests"
                    / "neetcode150"
                    / f"{problem.slug}_test.cpp"
                )
                self.assertTrue(harness.is_file())

    def test_challenge_markdown_is_readable_in_the_terminal(self) -> None:
        rendered = tracker.terminal_text(
            "# Title\n\n**Difficulty:** Easy\n\n## Example\n\n```text\n[1] -> false\n```"
        )
        self.assertIn("TITLE", rendered)
        self.assertIn("EXAMPLE", rendered)
        self.assertNotIn("**", rendered)
        self.assertNotIn("```", rendered)

    def test_review_intervals_lead_to_mastery(self) -> None:
        sessions = [session("2026-07-01")]
        self.assertEqual(
            tracker.next_review_date("duplicate-integer", sessions), date(2026, 7, 2)
        )

        sessions.append(session("2026-07-02", kind="review"))
        self.assertEqual(
            tracker.next_review_date("duplicate-integer", sessions), date(2026, 7, 9)
        )

        sessions.append(session("2026-07-09", kind="review"))
        self.assertEqual(
            tracker.next_review_date("duplicate-integer", sessions), date(2026, 7, 30)
        )

        sessions.append(session("2026-07-30", kind="review"))
        self.assertIsNone(tracker.next_review_date("duplicate-integer", sessions))
        self.assertEqual(
            tracker.mastered_slugs(self.catalogue, sessions), {"duplicate-integer"}
        )

    def test_assisted_attempt_is_due_again_tomorrow(self) -> None:
        sessions = [session("2026-07-01", outcome="helped")]
        self.assertEqual(
            tracker.next_review_date("duplicate-integer", sessions), date(2026, 7, 2)
        )

    def test_xp_counts_one_daily_check_in(self) -> None:
        sessions = [
            session("2026-07-01"),
            session("2026-07-01", "is-anagram", tests_passed=False),
        ]
        self.assertEqual(tracker.calculate_xp(sessions), 90)

    def test_streak_survives_until_the_next_day_ends(self) -> None:
        sessions = [session("2026-07-01"), session("2026-07-02", kind="review")]
        self.assertEqual(tracker.streaks(sessions, date(2026, 7, 3)), (2, 2))
        self.assertEqual(tracker.streaks(sessions, date(2026, 7, 4)), (0, 2))

    def test_duplicate_problem_day_is_rejected(self) -> None:
        progress = {
            "version": 1,
            "sessions": [session("2026-07-01"), session("2026-07-01", kind="review")],
        }
        with self.assertRaisesRegex(ValueError, "duplicates"):
            tracker.validate_progress(progress, self.catalogue)

    def test_progress_round_trip(self) -> None:
        progress = {"version": 1, "sessions": [session("2026-07-01")]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "progress.json"
            tracker.save_progress(progress, path)
            self.assertEqual(tracker.load_progress(self.catalogue, path), progress)

    def test_yuga_note_reads_like_a_sentence(self) -> None:
        note = tracker.compose_yuga_note(
            self.catalogue,
            {**session("2026-07-15"), "minutes": 34, "takeaway": "hash maps trade space for speed"},
        )
        self.assertEqual(
            note,
            "Contains Duplicate (new): solved independently in 34 min, tests passed."
            " Takeaway: hash maps trade space for speed",
        )

    def test_yuga_notify_is_skipped_without_a_token(self) -> None:
        opener = Mock(side_effect=AssertionError("must not touch the network"))
        original = tracker.urllib.request.urlopen
        tracker.urllib.request.urlopen = opener
        try:
            environment = dict(tracker.os.environ)
            tracker.os.environ.pop("YUGA_INGEST_TOKEN", None)
            try:
                tracker.notify_yuga(self.catalogue, session("2026-07-15"))
            finally:
                tracker.os.environ.clear()
                tracker.os.environ.update(environment)
        finally:
            tracker.urllib.request.urlopen = original
        opener.assert_not_called()

    def test_yuga_notify_failure_never_raises(self) -> None:
        original = tracker.urllib.request.urlopen
        tracker.urllib.request.urlopen = Mock(side_effect=OSError("network down"))
        try:
            environment = dict(tracker.os.environ)
            tracker.os.environ["YUGA_INGEST_TOKEN"] = "yuga_test"
            try:
                tracker.notify_yuga(self.catalogue, session("2026-07-15"))
            finally:
                tracker.os.environ.clear()
                tracker.os.environ.update(environment)
        finally:
            tracker.urllib.request.urlopen = original


if __name__ == "__main__":
    unittest.main()
