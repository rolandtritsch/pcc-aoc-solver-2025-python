"""Structured evidence prevents skipped/missing tests from advancing the CTO."""
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).parents[1]))
from aoc_python_evidence import answers, require_part, selection


class EvidenceTest(unittest.TestCase):
    def report(self, cases):
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "tests.xml"
        path.write_text("<testsuites><testsuite>" + cases + "</testsuite></testsuites>")
        return path

    def case(self, day, part, child=""):
        return (f'<testcase classname="tests.test_day{day:02}" '
                f'name="test_part{part}_sample">{child}</testcase>')

    def test_day00_only_selects_day01_part1(self):
        result = selection("Day00 - part1: 55\n", self.report(""), 0, 0)
        self.assertEqual((result["day"], result["part"]), (1, 1))

    def test_passing_part1_selects_part2(self):
        result = selection("Day01 - part1: 0\n", self.report(self.case(1, 1)), 0, 0)
        self.assertEqual((result["day"], result["part"]), (1, 2))

    def test_skipped_or_failed_tests_do_not_count(self):
        for child in ('<skipped/>', '<failure/>', '<error/>'):
            with self.assertRaises(ValueError):
                require_part(self.report(self.case(1, 1, child)), 1, 1)

    def test_unrelated_test_and_missing_part_do_not_count(self):
        with self.assertRaises(ValueError):
            require_part(self.report(self.case(1, 2)), 1, 1)

    def test_failed_named_part_selects_repair(self):
        result = selection("Day01 - part1: 1\n", self.report(self.case(1, 1, '<failure/>')), 0, 1)
        self.assertEqual((result["day"], result["part"]), (1, 1))

    def test_collection_runner_and_coverage_failures_block(self):
        for run_exit, test_exit in ((1, 0), (0, 2), (0, 1)):
            result = selection("Day01 - part1: 1\n", self.report(self.case(1, 1)), run_exit, test_exit)
            self.assertEqual(result["status"], "blocked")

    def test_duplicate_and_placeholder_runner_output_rejected(self):
        for text in ("Day01 - part1: 1\nDay01 - part1: 1\n", "Day01 - part1: TODO\n"):
            with self.assertRaises(ValueError):
                answers(text)

    def test_finale_is_not_day13(self):
        output = ""
        cases = ""
        for day in range(1, 13):
            for part in (1, 2):
                if (day, part) == (12, 2):
                    continue
                output += f"Day{day:02} - part{part}: 1\n"
                cases += self.case(day, part)
        result = selection(output, self.report(cases), 0, 0)
        self.assertEqual((result["day"], result["part"], result["stage"]), (12, 2, "finale"))


if __name__ == "__main__":
    unittest.main()
