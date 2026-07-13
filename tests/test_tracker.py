import importlib.util
import sys
import tempfile
import unittest
from collections import Counter
from datetime import date
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
