# Repository Intelligence and Read-Only Fact Finding

Use for an existing application, website, game, or meaningful feature change when accessible repository evidence could affect the design. Do not invent evidence for a new project with no code. The owner should not have to answer questions that code and project records can settle.

## 1. Locate one source of truth

1. Prefer the already-approved repository and branch. Recover the exact project from decisions, connected GitHub/GitLab access, project files or a local worktree. Do not pick a similarly named project without confirmation.
2. Record `repository`, `branch`, `HEAD` (when accessible), read authority, and any visibility limitations. Do not claim live connectivity based on a URL alone.
3. Read applicable project instructions (`AGENTS.md`, rules, specs), recent relevant issues and accepted decisions before forming design options. Respect private-data and credential boundaries.
4. If the repository is inaccessible, stop claiming implementation facts. Use available documents and label `EVIDENCE BLOCKED`; ask for access or one safe alternative only when it unlocks a material decision.

## 2. Inspect narrowly, following the user's end-to-end path

Use *read-only* search, listing, file reading and test inspection to answer only current high-value questions. Prioritize:
- Actual framework/runtime, folder topology and dependency declarations.
- Feature entry point and UI route -> API/service -> stored model/data -> authorization -> presentation/consumer.
- Existing utilities/components and established UX patterns that can be reused.
- Actual tests and CI scripts, data contracts, migration and compatibility constraints.
- Repo-local skill instructions or agent conventions and existing developer tasks.
- Critical risk evidence (e.g. mobile render cost, data denominator, role scoping or asset license).

For each consequential conclusion include evidence pointer (`path:line`, relevant commit/issue, or connected file reference); mention unreadable areas. Distinguish `IMPLEMENTED`, `PARTIAL`, `ABSENT IN SEARCHED SCOPE`, `UNVERIFIED`; never interpret missing search results as definite absence. Non-destructive reads only; do not run setup/build or mutate worktrees under Grill.

## 3. Optional parallel research, not automatic parallel coding

Delegated **read-only research subagents** are optional. Use them only if the current host explicitly supports them and the owner's permissions, data policy and cost budget permit. Never invent or announce a subagent run from a plan. Do not equate delegation with authorization to build or deploy.

Delegate *independent, bounded hypotheses* such as `UI route + interaction`, `API/data/auth semantics`, `tests/CI/performance`. Supply each read-only worker with exact repo/ref/scope, question, evidence format, stopping rule and budget; prohibit edits, dependency installs, destructive commands, pushes and credential collection. Request concise findings with confidence and path/line links.

Coordinator reconciles contradictory results, deduplicates observations and produces ONE repository evidence map. Parallelism is worthwhile only when its expected investigative benefit exceeds setup/coordination cost; if unavailable, inspect sequentially without asking the owner to organize agents.

## 4. Finish with a bounded evidence map

| Claim or unknown | Evidence | Status | Effect on goal / option | Next check |
|---|---|---|---|---|
| Existing comparison API | path:line or issue | VERIFIED / UNKNOWN | Reuse vs new endpoint | Bounded probe |

Stop browsing when further files will not change a significant choice, risk or acceptance test. Research does not authorize a repository change. For a new empty repository, replace code inspection with a feasibility spike proposal rather than fake path citations.
