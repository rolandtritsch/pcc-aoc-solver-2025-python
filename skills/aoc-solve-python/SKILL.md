---
name: aoc-solve-python
description: Implement or repair one assigned AoC 2025 Python part, verify named tests and exact runner output, and publish before handing off
---

Follow `aoc-workflow`, the `python-aoc-2025` checkout's `AGENTS.md`, applicable
project-local skills, and the latest review findings.

## Implement one authorized part

1. Read `problems/DayNNProblem.txt`, cached `inputs/DayNN.txt`, and official
   sample cases for the assigned part. Missing or locked rules block work.
2. Implement only that part in `src/aoc2025/dayNN.py`, using typed functions,
   separate parsing, meaningful preconditions, and algorithm/complexity docstrings.
   Preserve the other part and previous verified behavior.
3. Add `inputs/DayNNTest.txt` as needed and tests in `tests/test_dayNN.py`.
   Name part tests `test_part1_*` and `test_part2_*`; use official sample answers,
   independently checked boundaries, and real-input regressions. Remove skips
   only for implemented assigned work. An implementation's answer copied into a
   test is a regression assertion, not independent proof.
4. Update `src/aoc2025/main.py` to label only implemented parts as
   `DayNN - partP: <answer>`. Do not print fabricated numeric placeholders for
   unimplemented parts. Imports must stay silent.
5. Use the mandatory publication helper. It formats explicit intended Python
   files, including untracked ones, then checks Ruff, passing named tests for the
   assigned part, the full suite and coverage, and exact runner output.
6. On rejection, reproduce the defect from site/reviewer evidence, add a
   regression test, repair the same part, and repeat publication. Never guess
   another answer or start another part.

## Publication and handoff

Prepare a scratch JSON file containing a nonempty `description`: source task,
cycle start, canonical checkout, independent sample/edge evidence, material
paths, and relevant review findings. Include no credentials.

```bash
python3 <skill-base>/scripts/aoc_solver_publish.py publish \
  --day NN --part P --answer ANSWER --handoff /path/to/run-scratch/handoff.json
```

The helper uses injected `AOC_REPO_DIR` and Paperclip task/run credentials.
Default intended files are the day module, test module, sample input, runner,
and runner integration tests (`tests/test_main.py`). Extend the runner tests'
exact expected output when adding a part; retain the Day00 and prior-part
assertions. Do not remove or weaken those assertions to accommodate new output.
Use `--files` for an exact subset when a default file is absent or unintended.
Only intended files may be dirty or staged. Gatherer owns personal inputs and
problem statements. Additional assets or dependency changes need a reviewed
extension of the gate; never bypass it with manual Git/API calls.

The helper commits, checks committed formatting, pushes without force, and
verifies clean HEAD/tracking/live-remote equality. Only then does it create or
recover a same-part submitter issue. Record its receipt and confirmed handoff
before marking solving done. Failed push or ambiguous handoff keeps it unfinished.
Retry through the helper's stable source-task marker; never create duplicates
or discard another agent's work.

## Independent submitter verification

```bash
python3 <skill-base>/scripts/aoc_solver_publish.py verify \
  --day NN --part P --answer ANSWER --commit FULL_SOLUTION_HASH
```

Verification fetches origin, checks parity, Ruff, named day tests, full tests and
coverage, and the exact runner answer. It never formats source, commits, pushes,
or creates tasks. Failed, missing, skipped, or ambiguous evidence blocks submission.

## CTO progress evidence

After the review gate clears and Git is synchronized:

```bash
python3 <skill-base>/scripts/aoc_solver_publish.py progress --repo "$AOC_REPO_DIR"
```

This read-only mode runs the runner and full pytest suite independently. Its
summary records exit codes, current commit, and private diagnostic log paths.
Named tests are attributed by `tests/test_dayNN.py` and `test_partP_*`; missing,
skipped, or failed tests do not count. Both passing tests and one unambiguous
numeric runner result are required. Zero alone is neither a placeholder nor
proof. Day00-only evidence selects Day01 part1. Malformed evidence, collection
failures, and unattributed test/coverage failures fail closed. Day12 part2 is the
authenticated finale, never Day13 work.

The review gate still controls whether selection or same-part repair is allowed.
Stop after the authorized handoff; never wake the CTO.
