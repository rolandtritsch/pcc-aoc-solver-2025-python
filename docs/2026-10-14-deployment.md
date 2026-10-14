# Python company deployment — October 14, 2026

Created **AoC Solver 2025 Python** as a separate company, leaving the Scala
company and its seven agent configurations unchanged.

| Setting | Verified value |
| --- | --- |
| Company ID | `4d8990ae-ad0a-413c-81c1-b3e817fb0826` |
| Issue prefix | `AOCA` |
| Company UI | [AOCA][ui] |
| Private package | [pcc-aoc-solver-2025-python][package] |
| Solution repo | [python-aoc-2025][solutions] |
| Budget | `budgetMonthlyCents: 0` |
| Imported roster | Seven agents, all paused |
| Timers | All disabled |
| Runtime skills | Six company skills; Paperclip also installs its built-in skills |
| Future hiring | Board approval required |
| Runtime | Persistent uv 0.11.1 and Python 3.13.7 |

Canonical workspace:
`/paperclip/instances/default/workspaces/4d8990ae-ad0a-413c-81c1-b3e817fb0826/python-aoc-2025`.
Cycle start: `2026-10-14T12:24:51.480848+00:00`.
Package import revision: `719ec28832266e00fe028ab3e2cba15791cc28b3`.
Verified solution revision: `fca3e6a0622407deac170fbd2cbad45760521a8a`.

## Evidence

- 97 package regression tests passed, covering review gating, publication,
  structured Python progress evidence, and WatchDog behavior.
- Real uv/Ruff/pytest/JUnit/runner publication and independent verification passed
  against a temporary bare Git remote, without live task creation.
- The deployed checkout passed all 21 tests with 100% statement/branch coverage,
  Ruff checks, and exact Day00 execution.
- Deployed read-only progress selected Day01 part1 with both commands passing.
- All 13 imported Python script files matched package hashes. CTO and WatchDog
  launchers are executable; CTO delegated `--version` to OpenCode 1.18.31.
- Private package read access and dry-run solution push succeeded.
- All seven persisted agent configurations were checked directly without exposing
  credentials: models, provider JSON, matching helper models, fresh cycle,
  workspace, launcher paths, and company-scoped secret-reference bindings.
- The read-only live CTO gate returned ready. WatchDog telemetry had only
  `usage_trend_baseline_unavailable`, expected before its first report; it took no
  corrective action and performed no interpretation or report-writing.
- Separate Python vault entries reference the existing AWS backing credentials;
  no secret values were copied and no Pulumi/image redeployment was needed.
- Failed required-secret imports left partial records. Those records were deleted,
  then the package was imported with optional declarations and references bound
  afterward. Only one Python company remains.

Personal inputs remain tracked and pushed, matching the Scala repository by
explicit board choice. No input ignore rules were added.

No agents were invoked, puzzle tasks created, answers submitted, or models called.
Activation remains a separate explicit board action after checking funding and
runtime access. The company record itself is active; its entire agent roster is
paused and its automation timers are disabled.

[ui]: https://paperclip.tritsch.org/AOCA/dashboard
[package]: https://github.com/rolandtritsch/pcc-aoc-solver-2025-python
[solutions]: https://github.com/rolandtritsch/python-aoc-2025
