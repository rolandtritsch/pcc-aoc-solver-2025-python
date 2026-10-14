# Paused Python company deployment

## Import

Snapshot the Scala company before changes. Verify the Python name and slug are
unused. Preview explicitly with `target.mode: new_company` and
`newCompanyName: AoC Solver 2025 Python`, including company, agents, and skills.
Exclude `skills/company-creator/`, historical issues, and projects.

Apply the same reviewed source through `/api/companies/import` with
`pauseAutomations: true`. Record the new company ID, unique issue prefix, agent
IDs, and actual skill source directories. Do not retry an uncertain import before
checking whether the company already exists. Verify paused agents and disabled
timers before setup. Keep `budgetMonthlyCents: 0`, matching Scala.

## Persistent runtime

Install uv 0.11.1 in `/paperclip/.local/bin` and Python 3.13.7 in uv's persistent
Python directory. Verify both as the server user. Solutions use the pinned
interpreter, not the container's system Python 3.13.5.

Clone `rolandtritsch/python-aoc-2025` into
`/paperclip/instances/default/workspaces/<python-company-id>/python-aoc-2025`.
Use `main`, run `uv sync --locked`, and verify clean local/tracking/remote parity.
Never use the Scala checkout or copy Scala answers as Python solving evidence.

Set every agent's `cwd` and `AOC_REPO_DIR` to this checkout. Supply a fresh
timezone-aware `AOC_CYCLE_STARTED_AT`. Include `/paperclip/.local/bin` in PATH,
while preserving provider JSON and matching helper models.

Resolve CTO's command from its imported `aoc-workflow` directory, ending in
`scripts/aoc_cto.py`, and WatchDog's from its imported `aoc-watchdog` directory,
ending in `scripts/aoc_watchdog_runner.py`. Make both executable. Probe CTO with
`--version` to verify OpenCode delegation without inference. Set WatchDog's
`AOC_PAPERCLIP_UI_URL` to the public company UI root.

Create separate external-reference vault entries pointing at the existing AWS
OpenRouter, AoC session, and GitHub secrets. Bind the new IDs to the declared env
inputs. Do not copy secret values into files or logs. No Pulumi resource changes
or image redeployment are needed for this setup.

## Verify and leave paused

- Run Day00, full tests, and read-only progress. Initial selection is Day01 part1.
- Verify GitHub read and dry-run push access without changing remote commits.
- Check imported skills, launcher modes, CTO gate, and read-only WatchDog telemetry.
  Do not invoke its report-writing timer.
- Confirm seven agents, six runtime skills, unique company identity, no puzzle
  tasks or live runs, paused agents, and disabled timers. Compare the Scala snapshot.

Activation requires a later explicit board instruction. Check funding, runtime
access, and workspace readiness before enabling intended agents/timers.
