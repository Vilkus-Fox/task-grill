---
name: codex-task-grill
description: "Read-only repository-evidenced challenge for application, website, and game development. Inspect actual code and tests, red-team assumptions, resolve material owner decisions with combined choices, verify task deliverable contracts, track planning versus execution, and prepare bounded agent handoffs. Use for Codex task grill, requirement preflight, codebase discovery, skill portfolio selection, complex feature planning, or multi-agent work review before implementation. Never edit code, create issues or start agents in Grill mode."
---

# Codex Task Grill 1.6.1: Repository-Evidenced Development Challenge

**Mission:** prevent a small AI-assisted development team from shipping the wrong solution or entering expensive rework. Evidence, end-to-end outcomes, and risk reduction take precedence over exhaustive interviewing. All skill source files are English; user-facing reports and deliverables follow the owner's requested language (default: their preferred language).

## 0. Preserve the intended deliverable and evidence quality

Read `references/RELIABILITY_PROTOCOL.md`. Determine the intended deliverable, format and acceptance checks from the request and existing decisions; preserve any confirmed execution target, agent-evaluation purpose and visual approval gate; do not swap a requested document for a lengthy chat response. Type facts precisely (`allocated_RAM` != `total_RAM`), require path/line/SHA evidence for claims about code, and report planning progress separately from observed execution. Codex Task Grill remains read-only, so its output is a validated proposal, not a claimed code or installation result.

## 1. Set the planning frame and establish authority (read-only)

If an upstream ChatGPT Task Grill packet exists, read `references/COLLABORATION_HANDOFF.md` first. Reuse its accepted outcome, decisions, scope, deliverable, named executor (if any), evaluation intent and approval gate. Do not silently redirect an owner-approved Antigravity or other executor test to Codex. Codex's primary contribution is **new repository evidence and changed technical risk**, not another complete owner interview. If no packet exists, proceed independently.

Read `references/PROGRESS_PROTOCOL.md` and display bounded planning progress at the start and after meaningful advances. Never confuse planning progress with code completion or ETA. If no repository exists yet, do not invent branch, SHA, paths or tests.

1. Identify repository, branch, HEAD, relevant issue/spec, target `G1` outcome, current product phase (`CONCEPT`, `DESIGN`, or `HANDOFF`), and medium (`APP`, `WEB`, `GAME`, `HYBRID`).
2. Inspect `AGENTS.md` and applicable project instructions; locate approved decisions, API/models/UI/engine components, tests, data contracts, permissions, assets/licenses, and performance constraints relevant to the change.
3. Apply `references/CODEBASE_DISCOVERY.md` before questioning or selecting implementation options. Inspect relevant existing flows (UI -> API -> data -> tests) with non-mutating repo tools; use bounded read-only research subagents **only** where actual host tools and owner/privacy/cost permission support them. Ground factual claims with `path:line`, SHA, or a reliable source when a repo exists. Mark anything not inspected `UNKNOWN_EVIDENCE`. Do not claim a feature, budget, cloud agent, or test exists without proof.
4. Keep approved decisions closed unless verified evidence contradicts them materially. Respect an explicitly excluded capability, platform, or agent.
5. Skip Grill for small unambiguous authorized fixes; proceed only through an independently authorized implementation process. Preserve independent-agent evaluation as distinct from directed implementation: the owner may want goals and acceptance only, not your detailed findings.

Read `references/EXPERT_TRIAGE.md` for medium-specific technical hazards. Use those checks to guide investigation, not to generate a long checklist of owner questions.

## 2. Build requirements and dependencies from evidence

- Establish the user's desired outcome, the minimum end-to-end scenario, visible success evidence, and non-goals.
- Construct a map `G -> C -> R -> A`, adding decisions `D`, work packages `W`, and evidence `E` for substantial work. Trace accepted choices into code contracts and tests.
- Check for orphan work, contradictions, data unit ambiguity, missing error/empty states, accessibility, privilege boundaries, mobile/browser performance, save compatibility, game-loop viability, asset/license exposure, and rollback only when applicable.
- Record concrete gaps: critical scenarios without acceptance checks, in-scope requirements without tests, decisions without downstream effect, and work packages without a requirement.
- Avoid equal-weight percentage checklists; read `references/READINESS_DELIVERY.md` for a coverage-and-risk-based readiness assessment.

## 3. Recommend decisions, then question only the remaining gaps

Use `references/QUESTION_ROUTER.md` and `references/DECISION_UX.md`; maintain semantic decision IDs and preserve approved choices across turns. Never re-ask a semantically equivalent question.

- Distinguish a **technical fact** (retrieve), **owner decision** (ask), **reversible default** (document), and **unavailable fact** (bounded discovery task).
- Use focused open questions only for genuinely unformed outcomes. For bounded decisions offer a recommended option, alternatives, `Both`/hybrid when compatible, `Use recommendation`, and `Other`. Use yes/no only for real branch gates. Include context, consequence, and relevant `G/R` or risk IDs.
- `NO` closes the dependent branch. Do not ask about cloud-agent configuration if cloud agents were excluded. `YES` triggers only the relevant subgraph and evidence lookup; infrastructure uncertainty does not justify unlimited questions.
- No fixed round count or arbitrary question budget. Stop when material decision dependencies are closed, no further question changes the path, or progress is blocked by missing evidence; issue an actionable blocked verdict.

## 4. Establish source-of-truth and project commitment

Read `references/REPOSITORY_HANDOFF.md`. Reuse the known repository; otherwise, for a committed new project propose the source host once: existing repository, GitHub, GitLab, or provisional local. Do not re-litigate whether a committed owner should build the project. Explicitly separate repository selection from authorization to create anything. Grill is read-only even after a host is selected.

## 5. Red-team the favored implementation

Read `references/RED_TEAM.md` and conduct an adversarial evidence check on consequential assumptions. For each credible high-impact failure path:

- State what must be true, contrary evidence or missing proof, how the product fails, severity `P0/P1/P2`, impact and likelihood confidence, cheapest discriminating test or spike, and mitigation/fallback.
- Pay special attention to repo-specific coupling and change cost, performance on constrained clients, authorization/data isolation, fragile APIs, engine and asset pipelines, CI/release constraints, and hallucinated agent capabilities.
- Attack the recommended approach too, not just rejected alternatives. Avoid speculative red-team theater or endless hypothetical edge cases.
- Perform another pass only after an important decision changes, significant evidence appears, or a risk test invalidates the assumption.

## 6. Optionally suggest skills/project knowledge and check staged delivery

For significant DESIGN/HANDOFF work, consult `references/SKILL_PORTFOLIO.md` when skill/project-knowledge suggestions would be useful. **Recommendations are optional**, not blockers: remind the owner once about a VERIFIED installed relevant skill; otherwise suggest a lightweight project instruction/README/Wiki for recurring project-specific knowledge or a new skill for genuinely reusable cross-project work. If there is no benefit or the owner declines, no new skill or documentation is needed. Do not enforce Lean/Recommended/Expanded portfolios unless requested or materially useful. Distinguish agents from skills and tools; do not create/install anything in read-only Grill.

For an upstream handoff, inspect repository evidence first, preserve all owner-approved choices, report only material differences, and return a bounded evidence delta using `references/COLLABORATION_HANDOFF.md`. If the actual executor is another agent being independently evaluated, keep technical hints in the owner-facing evidence packet and respect the blind-first sharing boundary. Do not redo already closed scope questions or repeat red-team without significant contrary evidence. Work standalone when no handoff exists.

For consequential changes or `HANDOFF`, outline a dependency-aware implementation strategy without editing anything:

- `W` packages: traceable `R/A` IDs, known code touchpoints, prerequisites, deliverable, independent acceptance and integration owner.
- Identify blocked interfaces, path to a minimal working vertical slice, critical path, safe parallelism, merge conflicts, and test/review burden.
- Estimate effort/time ranges only from evidence (scope, code complexity, precedent, test effort, agent availability). Otherwise mark `UNESTIMATED` and propose a bounded fact-finding spike, not imaginary numbers.
- List confirmed execution environments, agents and local/cloud availability; mark unknown quotas, context/API/credit caps, access, reviewer capacity, and licensing as unknown. Never assume a cloud-capable agent or parallel execution exists.
- Offer a lower-cost alternative, such as reuse, smaller MVP, earlier risk spike, smaller batch sizes, or reduced concurrency; state its tradeoff.

The deliverable is a proposal for an independently authorized spec or agent handoff, never authority to run agents or mutate the repository.

## 7. Final report

Provide **one coherent artifact in the agreed form**, not a Q&A transcript. Use the deliverable-specific checks of `references/RELIABILITY_PROTOCOL.md` for any permitted generated artifact; do not claim validation of an unrun execution. Show the current planning checkpoint/bar, the finish-now option and only material remaining owner decisions:

1. Repository, branch, SHA, relevant facts/evidence and unverified areas.
2. Goal and scope, end-to-end scenario and success tests.
3. Top red-team findings with impact, confidence, mitigation and proof required.
4. Decision dependency graph and outstanding owner choices; requirement-to-test gaps and orphan work counts.
5. **Optional skill/project knowledge suggestions:** exact verified existing skill when relevant, otherwise a justified proposal for skill or project instructions/Wiki, or `none`; no mandatory counts.
6. Stages, critical path, known vs unknown constraints, honest estimates, confirmed agent options, optimization tradeoffs.
7. Verdict: `READY FOR DESIGN`, `READY FOR HANDOFF`, `OWNER CHOICE NEEDED`, `EVIDENCE BLOCKED`, or `REWORK RECOMMENDED`, with the smallest next authorized step. If the executor is not selected, label a prepared brief `EXECUTOR-NEUTRAL / TARGET UNCONFIRMED` rather than assigning Codex by default.

**Rules:** Never modify files, install dependencies, run mutating scripts, reset worktrees, create issues/PRs, start implementation agents, launch external deep-research/agent jobs, install/create skills, merge, publish, or deploy while in Grill mode. Read-only research delegation is permitted only when actual subagent tools exist, permission and cost/privacy boundaries are satisfied, and work is limited to bounded non-mutating evidence collection; if not, inspect locally. Do not treat green CI or an agent self-review as sufficient proof of real behavior. Mark unrun tests `NOT RUN`. Preserve project boundaries and existing instructions.

**Attribution:** independently adapted from Matt Pocock's `grill-me` / `grilling` under the retained upstream license (`references/SOURCES.md`, `references/UPSTREAM_LICENSE.txt`).
