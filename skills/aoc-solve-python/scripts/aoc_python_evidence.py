"""Read pytest JUnit evidence and runner output without guessing puzzle progress."""

import re
import xml.etree.ElementTree as ET


def test_results(path):
    """Return per-part results; only named tests in per-day modules count."""
    if path.stat().st_size > 4 * 1024 * 1024:
        raise ValueError("pytest report exceeds the evidence limit")
    try:
        root = ET.parse(path).getroot()
    except ET.ParseError as error:
        raise ValueError("Invalid pytest XML") from error
    parts = {}
    for case in root.iter("testcase"):
        day = re.search(r"(?:^|\.)test_day(\d{2})(?:\.|$)", case.get("classname", ""))
        part = re.match(r"test_part([12])_", case.get("name", ""))
        if not day or not part:
            continue
        key = (int(day[1]), int(part[1]))
        counts = parts.setdefault(key, {"passed": 0, "failed": 0, "skipped": 0})
        if case.find("failure") is not None or case.find("error") is not None:
            counts["failed"] += 1
        elif case.find("skipped") is not None:
            counts["skipped"] += 1
        else:
            counts["passed"] += 1
    return parts


def passing(counts):
    """A part must have passing named tests and no failed or skipped named tests."""
    return counts.get("passed", 0) > 0 and not counts.get("failed") and not counts.get("skipped")


def require_part(path, day, part):
    if not passing(test_results(path).get((day, part), {})):
        raise ValueError("Assigned part has no complete passing active test evidence")


def answers(output):
    result = {}
    for day, part, answer in re.findall(r"^Day(\d{2}) - part([12]):\s*(\S+)\s*$", output, re.M):
        key = (int(day), int(part))
        if key in result:
            raise ValueError("Runner reports the same part more than once")
        if not re.fullmatch(r"\d+", answer):
            raise ValueError("Runner reports a nonnumeric or unimplemented answer")
        result[key] = answer
    return result


def selection(output, report, run_exit, test_exit):
    """Select the first uncertain part; unrelated command failures fail closed."""
    values = answers(output)
    results = test_results(report)
    if run_exit or test_exit not in (0, 1) or not values:
        return {"status": "blocked", "reason": "Runner or test collection failed; reconcile command evidence"}
    if test_exit and not any(c["failed"] for c in results.values()):
        return {"status": "blocked", "reason": "Test/coverage failure cannot be attributed to a named puzzle part"}
    for day in range(1, 13):
        for part in (1, 2):
            counts = results.get((day, part), {})
            if (day, part) not in values or not passing(counts):
                return {"status": "ready", "day": day, "part": part,
                        "stage": "finale" if (day, part) == (12, 2) else "solve",
                        "reason": "Earliest part lacks successful current runner/test evidence",
                        "tests": counts, "runnerPresent": (day, part) in values}
    return {"status": "blocked", "reason": "Finale requires authenticated acceptance and review, not numeric output"}
