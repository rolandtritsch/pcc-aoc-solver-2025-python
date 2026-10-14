# AoC Solver 2025 Python

A [Paperclip][] company that implements tested Python solutions in
[python-aoc-2025][solutions] for [Advent of Code 2025][aoc], through Day12.
Adapted from [the Scala company template][template] with a fresh history.

## Company and workflow

Company name: **AoC Solver 2025 Python**. Portable slug:
`aoc-solver-2025-python`. Import it as a **new company**, preserving the Scala
company. The server allocates a distinct issue prefix.

| Agent | Responsibility | Reports to |
| --- | --- | --- |
| CTO | Authorizes one part or same-part repair per later wake | — |
| Problem Gatherer | Gathers assigned rules, personal input, and samples | CTO |
| Problem Solver | Implements and publishes a verified Python part | CTO |
| Problem Submitter | Verifies publication and obtains the site's verdict | CTO |
| Solution Reviewer | Reviews verdicts and validated reusable improvements | CTO |
| WatchDog | Independent report-only observer | — |
| Model Tester | Manually assigned routing/model probe | — |

**CTO → gather if needed → solve → submit → review → wait.** No next part starts
before a completed accepted review. A rejection permits only a reviewed same-part
repair on a later CTO wake. Day00 is the template. Day12's finale follows the
site's authenticated instructions rather than an invented computation.

The [workflow][] provides duplicate-safe handoffs and disposition rules. The
[publication helper][solver] formats intended Python files, checks Ruff, named
part tests, full tests/coverage, and the exact runner answer, commits, pushes, and
checks remote parity before handing off. Submitter verifies it independently.
CTO progress is parsed from runner output and pytest JUnit results; missing or
skipped tests cannot advance the cycle.

The [reviewer][] commits bounded, validated improvements into the solution repo's
`skills/` and `scripts/`, with discovery guidance in `AGENTS.md`. The [WatchDog][]
retains deterministic report persistence and bounded optional interpretation; it
takes no corrective action and its reports never authorize puzzle work.

## Models, inputs, and secrets

Problem Solver uses `deepseek/deepseek-v4-pro-0813`; the other six use
`deepseek/deepseek-v4-flash-0731`, all through `opencode_local`. The manifest keeps
the template's OpenRouter mapping and matching helper models. These are inherited
choices, not a new Python-specific model evaluation.

Each company has its own vault references to the existing AWS-backed credentials:
`OPENROUTER_API_KEY`, `AOC_SESSION` for gatherer/submitter, and `GH_TOKEN` for agents
that use GitHub. Values stay in AWS Secrets Manager, managed by
[pulumi-paperclip][infra]. Never reuse Scala-company vault IDs or copy credentials.
Declarations are optional during import so existing external references can be
bound afterward; deployment must verify all required bindings before activation.

The same AoC account can have accepted Scala answers. Python solving and testing
remain independent. Matching existing acceptance is confirmed without reposting;
a mismatched answer blocks submission for reconciliation.

Personal inputs in `inputs/DayNN.txt` and samples in `inputs/DayNNTest.txt` are
tracked and pushed to the public solution repo, matching Scala by explicit board
choice. No input ignore rules are introduced.

## Import and deployment

Preview from this checkout:

```bash
paperclipai company import . --target new \
  --new-company-name "AoC Solver 2025 Python" --dry-run
```

Apply the reviewed package through the authenticated board import API with
`pauseAutomations: true`, importing company, seven agents, and six runtime skills.
Exclude developer-only `company-creator`, historical issues, and projects. See
[deployment][] for preparation and verification. Deploy the solution checkout
independently of the package import.

The manifest omits workspace IDs, launcher commands, and cycle timestamps.
Deployment supplies `cwd`, `AOC_REPO_DIR`, a fresh `AOC_CYCLE_STARTED_AT`, actual
imported launcher paths, and company-scoped secret references. Every agent starts
paused and every timer disabled. CTO's interval is five minutes; WatchDog's is
ten. Activation is a separate explicit board action.

uv 0.11.1 and Python 3.13.7 live on the persistent `/paperclip` volume. The Python
checkout uses its lockfile. PATH includes `/paperclip/.local/bin`. Recheck
executable launcher modes after skill replacement.

## Validation

```bash
python3 -B -m unittest discover -s skills/aoc-workflow/scripts/tests -v
python3 -B -m unittest discover -s skills/aoc-solve-python/scripts/tests -v
python3 -B -m unittest discover -s skills/aoc-watchdog/scripts/tests -v
```

Tests use offline fixtures and temporary bare remotes, without site submission,
live task creation, or model inference. Reusable research is retained; historical
Scala-run reports are excluded. Local developers can discover `company-creator`
through `.claude/skills/` and `.agents/skills/` symlinks.

[Paperclip]: https://github.com/paperclipai/paperclip
[solutions]: https://github.com/rolandtritsch/python-aoc-2025
[aoc]: https://adventofcode.com/2025
[template]: https://github.com/rolandtritsch/pcc-aoc-solver-2025
[workflow]: skills/aoc-workflow/SKILL.md
[solver]: skills/aoc-solve-python/SKILL.md
[reviewer]: skills/aoc-review/SKILL.md
[WatchDog]: skills/aoc-watchdog/SKILL.md
[infra]: https://github.com/rolandtritsch/pulumi-paperclip
[deployment]: docs/deployment.md

## Season completion

The 2025 edition ends at Day12. Once all 24 day/part reviews in the current
cycle are accepted with no repair required, the CTO gate returns `complete` and
the launcher exits successfully before inference. No further gatherer task or
Day13 work starts. The Day12 finale is verified through authenticated site
evidence and review, without requiring a fabricated numerical answer.
