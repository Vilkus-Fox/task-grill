---
name: antigravity-task-grill
description: "Read-only evidence-based task challenge for Google Antigravity App, CLI and IDE. Use before implementing a consequential app, website or game feature to inspect available repository evidence, preserve approved owner decisions, challenge technical and product risks, and prepare bounded implementation handoffs. Never edit project files, create issues or PRs, launch agents, or deploy while grilling."
---

# Antigravity Task Grill 1.6.1: Read-only Pre-implementation Challenge

**Mission:** find real evidence, protect already-approved decisions, and improve the next implementation task without turning analysis into implementation. Follow the owner's preferred output language. This skill is a preview, not a guarantee of model behavior.

## A. Confirm scope and actual host access

1. Determine the requested outcome and deliverable (concept decision, design recommendation, or handoff), target executor, acceptance evidence and explicit exclusions. Do not automatically assign implementation to Antigravity just because this skill runs there.
2. Read `references/RELIABILITY_PROTOCOL.md` and `references/PROGRESS_PROTOCOL.md`. Show honest bounded **planning** progress separately from independently observed **execution** progress.
3. Inspect available workspace rules (`AGENTS.md`, `GEMINI.md`, applicable local rules) without changing them. Discover which read-only workspace, search, terminal or repository tools this session actually exposes. A feature mentioned in Antigravity documentation is not proof that it is enabled here.
4. Treat **Grill mode as strictly read-only**. No editing source or documentation, generating persistent project artifacts, installs, agents/subagents, commits, issues, PRs, merges or deployment. No shell commands that modify a worktree, caches, credentials, infrastructure or services. If a tool would mutate, do not call it. If requested to implement, close the Grill assessment and require a distinct, explicitly authorized execution workflow.

## B. Verify evidence before asking questions

1. Recover prior owner-approved decisions and scope from accessible conversation, files and authorized repositories. Read `references/COLLABORATION_HANDOFF.md` if a ChatGPT/Codex packet exists; reuse decisions and verified evidence, checking material deltas only. Never repeat a settled interview.
2. For existing projects inspect actual code/tests/contracts before making file-specific claims. Read `references/CODEBASE_DISCOVERY.md`; use narrow searches and targeted file ranges. If the workspace, private repository or tool is inaccessible, label it `UNKNOWN_EVIDENCE`; do not hallucinate file contents, commits, CI or permissions.
3. Attach a path, line, commit or source to verified code claims when available. Distinguish `VERIFIED`, `APPROVED`, `ASSUMED`, `OPEN`, and `UNKNOWN_EVIDENCE`. For evidence imported from another agent, retain the original source and SHA; label `NOT_REVERIFIED_BY_RECIPIENT` until independently checked.
4. Recover required output format, executor selection, evaluation intent and visual approval gates. If the owner is testing an agent independently, keep a `BLIND_FIRST` brief: goal, boundaries and acceptance tests, not a pre-solved file map.

## C. Apply bounded product and architecture challenge

1. Choose `CONCEPT`, `DESIGN` or `HANDOFF`; classify `APP`, `WEB`, `GAME` or `HYBRID`. For small, explicit, already-approved fixes, skip the grill and advise the ordinary authorized delivery path.
2. Use `references/EXPERT_TRIAGE.md`, `references/QUESTION_ROUTER.md`, and `references/DECISION_UX.md`. Map `G -> C -> R -> A` (goal, capability, requirement, acceptance), with decisions and evidence when useful.
3. Research technical facts first. Ask only consequential unresolved owner choices, offer a recommendation and compatible combinations, and do not reopen a rejected branch. An evidence blocker is not a reason for repetitive questions.
4. Use `references/RED_TEAM.md` for credible failure scenarios and cheapest falsification checks. Test your own favored solution. Consider permission/privacy, runtime limits, tool trust, dependency and licensing risks where material; avoid fabricated scores or quotas.
5. Read `references/REPOSITORY_HANDOFF.md`, `references/READINESS_DELIVERY.md` and optionally `references/SKILL_PORTFOLIO.md`. Suggest optional skills only when useful; do not create or install them in Grill mode.

## D. Produce a single useful handoff

- Deliver a compact goal/scope statement, supported evidence with provenance, accepted decisions, highest-impact risks, acceptance-backed work packages, dependencies, unresolved material decisions and cheapest next verification.
- Preserve the chosen executor (Antigravity, Codex, another agent, or `EXECUTOR-NEUTRAL / TARGET UNCONFIRMED`) and any owner approval gates.
- Use `READY FOR DESIGN`, `READY FOR HANDOFF`, `OWNER CHOICE NEEDED`, `EVIDENCE BLOCKED` or `REWORK RECOMMENDED`, without confusing a planning verdict with successful execution or authorization.
- Do not claim files changed, tests passed or agents launched. Label unrun checks `NOT RUN`. Stop when evidence and consequential decisions are sufficient, not after a fixed number of questions.

## E. Antigravity installation and first-use evaluation

- Workspace: copy this entire **standalone** skill folder to `<workspace-root>/.agents/skills/antigravity-task-grill/` (including its `references/` files). Global Antigravity App/IDE: `~/.gemini/config/skills/antigravity-task-grill/`. Prefer workspace scope for the pilot; do not install globally without consent.
- In Antigravity App use `/antigravity-task-grill` or ask the agent to invoke it. In Antigravity IDE/CLI consult current skill discovery and slash-command support; reload skills/start a new session when needed.
- First live pilot: give a real but bounded problem, verify that the correct skill is activated, workspace evidence is read only, earlier decisions are preserved, and the handoff is actionable. Compare a matched run without the skill where possible. Report correctness, unsupported claims, repeated questions, elapsed time, available resource metrics and `adopt/revise/disable`. If Antigravity is not accessible, state `LIVE PILOT NOT RUN`.
- External scripts are not required for this skill and must not be executed merely to activate it.

**Sources:** common references and licenses bundled with Task Grill; official platform guidance: https://antigravity.google/docs/skills .