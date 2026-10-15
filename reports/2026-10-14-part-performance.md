# AoC 2025 Python current-run timing and tokens

Snapshot: **October 14, 2026, ~17:40 UTC** (live Paperclip query, company `AoC Solver 2025 Python` / `4d8990ae-ad0a-413c-81c1-b3e817fb0826`).

**9 parts have finished solver, submit, and review runs, all `done`:**
Day01 part1 + part2, Day02 part1 + part2, Day03 part1 + part2,
Day04 part1 + part2, Day05 part1.
Day05 part2 and later days have no puzzle assignments in this snapshot.

The solver ran **9 primary runs totaling ~41m 16s (2,475.5s)** and
**7,915,618 recorded tokens**, including **6,581,299 cached input tokens
(83.1%)**. Counting the superseded Day01 part1 retry, solver work is
~55m 56s and 9,440,781 tokens. These are agent-run measurements
(`startedAt` to `finishedAt`, incl. reading, implementation, tooling,
tests, git, handoff), not pure algorithm time or a provider invoice.

## Scope and measurement

- **Solver elapsed:** primary solver run `startedAt` to `finishedAt`.
  Day01 part1 has two succeeded solver runs; the table uses the final
  `eefbeb22` (4m 19s). The superseded `5a20ead4` (14m 41s, 1,525,163
  tokens) is kept in the run-usage CSV and included in that part's
  pipeline total, but excluded from the solver totals above.
- **Gather -> reviewed:** first part issue creation (`createdAt` of the
  gather issue, or the solve issue for part 2s which have no gather) to
  review-run `finishedAt`. Part 2s reuse the part 1 input, so their
  `gather` cell is empty.
- **Tokens:** `usageJson.inputTokens` (fresh), `usageJson.cachedInputTokens`
  (re-served context, counted again per step), `usageJson.outputTokens`.
  Total = fresh + cached + output. This DeepSeek-via-OpenRouter adapter
  reports no separate reasoning or step counts, so `reasoning` and `steps`
  are blank (not zero-claimed).
- **Stage total (`pipelineTokens`):** recorded tokens from the part's
  gather + solve (+ retry) + submit + review runs. CTO assignment runs
  (one per part, `ctx=None`) are excluded for comparability with the
  Scala report; WatchDog/monitoring runs are out of scope. All 34
  stage runs have usage objects and `succeeded` status.

## Every solved day and part

Durations in seconds; tokens are exact recorded counts.

| Part / solve task | Solver elapsed | Gather -> reviewed | Fresh input | Cached input | Output | Solver total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Day01 part1 (AOCA-3, final `eefbeb22`) | 259.189 (4m 19s) | 2355.652 (39m 16s) | 131,624 | 272,128 | 40,920 | **444,672** |
| Day01 part2 (AOCA-9) | 94.347 (1m 34s) | 1182.704 (19m 43s) | 73,042 | 513,792 | 6,670 | **593,504** |
| Day02 part1 (AOCA-15) | 226.496 (3m 46s) | 1123.627 (18m 44s) | 80,167 | 681,216 | 11,302 | **772,685** |
| Day02 part2 (AOCA-20) | 226.203 (3m 46s) | 1472.609 (24m 33s) | 149,647 | 421,427 | 6,831 | **577,905** |
| Day03 part1 (AOCA-28) | 345.09 (5m 45s) | 1581.997 (26m 22s) | 74,895 | 1,435,648 | 14,614 | **1,525,157** |
| Day03 part2 (AOCA-33) | 382.793 (6m 23s) | 1340.731 (22m 21s) | 472,212 | 361,472 | 15,002 | **848,686** |
| Day04 part1 (AOCA-40) | 255.776 (4m 16s) | 1760.71 (29m 21s) | 88,283 | 724,992 | 11,365 | **824,640** |
| Day04 part2 (AOCA-47) | 324.961 (5m 25s) | 1627.83 (27m 08s) | 51,433 | 937,216 | 13,072 | **1,001,721** |
| Day05 part1 (AOCA-55) | 360.632 (6m 01s) | 2164.421 (36m 04s) | 79,036 | 1,233,408 | 14,204 | **1,326,648** |

Superseded retry (in pipeline total and run-usage CSV only):
Day01 part1 `5a20ead4`, 880.72s (14m 41s), 211,239 / 1,268,480 / 45,444 = 1,525,163.

## Recorded tokens across specialist stages (CTO excluded)

| Part | Stage total | Runs (usage / associated) | Note |
| --- | ---: | ---: | --- |
| Day01 part1 | 6,113,822 | 5 / 5 | incl. both solver runs |
| Day01 part2 | 3,743,275 | 3 / 3 | no gather issue |
| Day02 part1 | 3,829,314 | 4 / 4 | — |
| Day02 part2 | 4,416,470 | 3 / 3 | no gather issue |
| Day03 part1 | 5,333,488 | 4 / 4 | — |
| Day03 part2 | 3,413,353 | 3 / 3 | no gather issue |
| Day04 part1 | 4,890,082 | 4 / 4 | — |
| Day04 part2 | 5,563,102 | 4 / 4 | — |
| Day05 part1 | 5,729,503 | 4 / 4 | — |

Across all parts these stages recorded **43,032,409 tokens**
(7,915,618 solver + 35,116,791 gather/submit/review, counting the
Day01 part1 retry in the stage total).

Largest solver runs by all recorded tokens: Day03 part1 (1,525,157),
Day05 part1 (1,326,648), Day04 part2 (1,001,721).
Largest fresh-input runs: Day03 part2 (472,212), Day02 part2 (149,647),
Day01 part1 final (131,624).

## Evidence and reproducibility

- [Per-part CSV](2026-10-14-part-performance.csv): exact UTC timestamps,
  durations in seconds, token components, primary solver run IDs, stage
  totals and coverage. `reasoning`/`steps` are blank: not reported by
  this adapter.
- [Per-run usage CSV](2026-10-14-part-run-usage.csv): all 34
  task-associated specialist runs (CTO runs excluded), status, UTC times,
  recorded token components. Day01 part1 appears twice (retry + final).
- Metrics were read from `paperclipai issue runs <id> --profile python
  --json` (`usageJson`) on 2026-10-14 ~17:40 UTC. Live state may advance
  after this cutoff.
- Agent IDs: solver `70217589…`, gatherer `e0d65cba…`, submitter
  `3a4a4365…`, reviewer `cb9f3828…`, CTO `57fc3151…` (excluded from
  stage totals).
