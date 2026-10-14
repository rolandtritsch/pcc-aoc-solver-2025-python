# Python company activation — October 14, 2026

The board explicitly authorized activation after the readiness checks. Six agents
are enabled: CTO, Problem Gatherer, Problem Solver, Problem Submitter, Solution
Reviewer, and WatchDog. Model Tester remains paused.

- CTO timer: enabled, every 300 seconds.
- WatchDog timer: enabled, every 600 seconds; non-timer wakeups remain disabled.
- Specialists wake on assignments; their periodic timers remain disabled.
- The Scala company's configuration and all seven agents are unchanged.
- Portable package import defaults remain paused with disabled timers.

## First cycle evidence

The first manual CTO wake (`746356a2-912c-437f-929d-5003ba3bc3e7`) succeeded and
authorized Day01 part1 only. [AOCA-2][gather] gathered the material successfully.
[AOCA-3][solve] implemented and published the part, with 43 tests passing.
[AOCA-4][submit] independently verified publication and confirmed the account's
existing accepted answer without reposting it. [AOCA-5][review] reached review;
its status at this activation check is `in_progress`.

[AOCA-6][watchdog] is the first successfully persisted timer report. No corrective
action was taken by WatchDog.

The first Python part revealed that runner integration tests also need to be
included in publication's intended-file allowlist. The gate now permits and
formats `tests/test_main.py`, and its default list includes the file. Existing
Day00 and prior-part assertions must remain intact. The correction was tested
with 22 publication/evidence regressions, published in this package, deployed to
the Python solver skill only, and noted on AOCA-3.

The live review gate returned `wait` while the first review was unfinished. The
CTO timer runs behind that guard and authorizes nothing further until the cycle
has a completed accepted review and no active specialist run. After all 24 parts
through Day12 have accepted completed reviews, the terminal guard exits before
inference and starts no further gathering or Day13 work.

[company]: https://paperclip.tritsch.org/AOCA/dashboard
[gather]: https://paperclip.tritsch.org/AOCA/issues/AOCA-2
[solve]: https://paperclip.tritsch.org/AOCA/issues/AOCA-3
[submit]: https://paperclip.tritsch.org/AOCA/issues/AOCA-4
[review]: https://paperclip.tritsch.org/AOCA/issues/AOCA-5
[watchdog]: https://paperclip.tritsch.org/AOCA/issues/AOCA-6
