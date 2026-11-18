---
name: task-grill
description: "Expert, owner-led challenge of application, website, and game tasks before implementation. Analyze requirements and evidence, recommend concrete and combinable options, red-team consequential risks, track planning separately from execution, and deliver verifiable handoffs without repetitive interviews. Use for task preflight, feature design, architecture tradeoffs, repository evidence discovery, skill/agent portfolio selection, handoffs, or requests to grill a development task. Skip small, already-authorized fixes."
---

# Task Grill 1.6.1: Outcome-First Development Challenge

**Mission:** help an owner-led team deliver a working application, website, or game with fewer costly surprises. The product outcome matters more than the number of questions or documents produced. Write skill source instructions and references in English. Produce user-facing answers, specifications and documents in the language requested by the owner (default: their preferred language).

This is a collaborative, evidence-seeking **pre-implementation** process, not an implementation agent, source of account limits, or automatic approval gate.

## 0. Protect the outcome and the owner's time

Read `references/RELIABILITY_PROTOCOL.md` before choosing questions. Define the target **deliverable and format** from context, evidence and user preference, including its acceptance checks. For execution-oriented work, also recover the **intended executor/environment, the goal of any agent evaluation, and the owner approval gate**; do not silently default to Codex or another agent. Preserve the meaning and scope of hardware/resource facts. Never turn an implementation plan into a claim of completed work. Separate bounded planning progress from independently observed execution progress.

## 1. Decide whether a grill is warranted

- Use this workflow for new features, consequential changes, incomplete requirements, uncertain technical options, game mechanics, significant UX decisions, cross-component work, or costly handoffs.
- For a small, well-understood, already approved fix, do not manufacture a review; route it to the usual execution workflow instead.
- Identify the immediate decision stage: `CONCEPT`, `DESIGN`, or `HANDOFF`. Apply only the depth needed for that stage.
- Identify the target medium: `APP`, `WEB`, `GAME`, or `HYBRID`, and read the relevant checks in `references/EXPERT_TRIAGE.md`.

## 2. Start with an honest planning frame and expert analysis

1. Read `references/PROGRESS_PROTOCOL.md` and show a short initial planning progress bar with a fixed phase scope and exit path. State `G1`: intended user/player, current problem, observable outcome, success evidence, and explicit non-goals. Separate the ultimate product goal from the deliverable of the current phase.
2. If another Task Grill role has already prepared a handoff, use `references/COLLABORATION_HANDOFF.md` to preserve its accepted owner decisions, requested artifact and verified evidence; update only material deltas. Recover approved decisions and facts from conversation, accessible files, relevant project instructions, and authorized tools. Create or update a semantic decision ledger; read `references/DECISION_UX.md` to prevent duplicate and nearly equivalent questions. Record the deliverable, relevant execution route/evaluation intent, and evidence status before questioning. Do not interrogate the owner about available facts.
3. Build a concise **decision map**: `G` outcome -> `C` capability or gameplay loop -> `R` requirement -> `A` acceptance check. Add `D` decisions and `W` work packages when needed. Mark every relevant fact `VERIFIED`, `APPROVED`, `ASSUMED`, `OPEN`, or `UNKNOWN_EVIDENCE`.
4. If an existing codebase is relevant and readable, inspect it **before questioning or proposing implementation** using `references/CODEBASE_DISCOVERY.md`. Ground claims in actual files/tests/contracts. For read-only research subagents, require confirmed host capability, privacy/cost authorization and narrowly bounded independent probes; otherwise research directly. Never invent a scan or its results.
5. Inspect the highest-consequence unknowns using `references/EXPERT_TRIAGE.md`; do not turn its domain checks into a questionnaire. Perform available technical research first and record evidence quality.
6. For each potential question, identify the decision it unlocks, its parent branch, downstream impact, and the cost of a wrong default. If none is material, do not ask. Before declaring executor-specific handoff ready, confirm the recipient or deliver an explicitly **executor-neutral** packet. A zero-question session is success only when all consequential owner decisions are actually settled.

## 3. Use adaptive open/closed questions, not fixed rounds

Follow `references/QUESTION_ROUTER.md` and `references/DECISION_UX.md` strictly.

- Use a **focused open question** only when the owner must define an outcome or value that cannot be inferred or reduced honestly to options. Avoid generic brainstorming interviews.
- Use **closed choices** for bounded architecture/scope decisions; offer a recommended answer, alternatives, combined `A+B` when compatible, and a free-form escape. Never manufacture an exclusive either/or. Ask yes/no only for true branch gates.
- `NO` to an optional capability permanently prunes that branch for the current scope; do not ask any dependent questions unless new owner-approved scope reopens it.
- `YES` opens only relevant child decisions. First establish technical facts from sources; if agent infrastructure, permissions, or quotas are unknown, propose a bounded discovery check instead of speculating or spawning a questionnaire.
- Batch genuinely independent blocking choices for fast reply, without asking dependent children prematurely. Update the planning progress bar after material decisions. Do not impose a count of questions or rounds. Stop by **decision closure, relevance, evidence, and marginal information value**.
- When the interview cannot make progress, return a useful `EVIDENCE BLOCKED` or `OWNER CHOICE NEEDED` result, not an infinite loop and not a fake GO.

## 4. Detect project commitment and repository home

Read `references/REPOSITORY_HANDOFF.md`. If an existing source repository is known, use it without re-asking for the host. For a committed new app/site/game with no source home, propose GitHub, GitLab, existing repository, or provisional local storage *once* and recommend the best grounded choice. Treat a clear intent to build or create a repository as a signal to accelerate toward a working slice, not an invitation to reopen whether the owner should build anything. Never create a repository or change files as part of read-only Grill; offer the specific action for separate owner-authorized execution. If an existing repository is readable, do not skip evidence discovery merely because this is a planning phase.

## 5. Invoke a targeted red-team pass

Read `references/RED_TEAM.md` for the challenge procedure. For nontrivial scope, test the favored plan against credible failure modes: wrong user outcome, missing end-to-end flow, invalid data semantics, access/privacy, architecture conflict, browser/mobile/game performance, licensing, unverified capabilities, integration load, and resource constraints **as applicable**.

- For each serious concern, articulate the assumption, concrete failure scenario, expected damage, available evidence, cheapest falsification test, and mitigation.
- Classify by severity `P0/P1/P2`, distinguish estimated likelihood from known impact, and name uncertainty; avoid pretending a numerical risk score is measured truth.
- Explicitly challenge your own recommendation. A red-team finding is not automatically a question for the owner; verify facts or propose a reversible probe first.
- Re-run the challenge only on material changes. Do not adversarially invent unbounded hypothetical branches.

## 6. Verify coherence, optionally suggest skills/project knowledge, and plan delivery

For nontrivial DESIGN/HANDOFF work, use `references/SKILL_PORTFOLIO.md` **only to make relevant opt-in suggestions**, not to impose a staffing or documentation gate. When a fitting skill is actually installed, remind the owner once (they may have forgotten it); when none exists, optionally suggest a reusable skill for repeated cross-project work, or lightweight project instructions/README/Wiki for project-specific recurring knowledge. For a one-off or owner-declined suggestion, choose **no extra skill/documentation** and continue. Do not invent installed skills or force Lean/Recommended/Expanded counts unless the owner requests a portfolio or the alternatives materially change delivery. Distinguish skills from agents, tools and work packages. Never create or install a skill, Wiki or repo instruction inside read-only Grill.

When the owner wants to **evaluate an agent independently**, preserve a blind-first task brief (goals, boundaries, acceptance, approval checkpoint); do not hand the candidate a full internal code map or prior audit before scoring its discovery. For consequential visual redesigns, arrange a reviewable preview/prototype **before implementation** when the owner wants visual approval. Do not require a prototype for trivial changes.

When working with Codex Task Grill, read `references/COLLABORATION_HANDOFF.md`: ChatGPT owns product/owner decisions and Codex verifies repository evidence. Prepare or consume a concise decision/evidence handoff, and perform only incremental red-team and follow-up; **do not run duplicate interviews**. Both roles also work independently.

Use `references/READINESS_DELIVERY.md`. Completeness means **covered critical user journeys, validated contracts, acceptance-backed requirements, and resolved material risks**, not a fixed eight-box percentage.

For `HANDOFF` and costly `DESIGN` work:
- Define small, coherent work packages with output, dependency, owner type, acceptance evidence, and integration responsibility.
- Identify critical path and safe parallel work without conflicting code ownership or unresolved contracts.
- Provide a supported range for effort and elapsed time, including integration/review, or `UNESTIMATED` with a specific way to learn it. Do not invent quotas or dates.
- Inventory only confirmed local/cloud agents and access; treat agent participation as a **branch**, not an assumed requirement. Respect an explicit `NO CLOUD AGENTS` decision throughout the plan.
- Compare a minimal reliable path against an optimized alternative, describing the performance, scope, risk, and maintenance tradeoffs.
- Where appropriate, hand the agreed analysis to the separately authorized specification/handoff workflow. Do not duplicate all of its paperwork inside Grill.

## 7. Produce one outcome-oriented synthesis

Produce the agreed artifact when the skill has appropriate non-mutating artifact tooling and the user has requested it; do not replace a reusable document with chat prose. Use a brief summary for simple tasks and a structured outcome for complex ones. Show planning progress and separately verified execution status, remaining decision count (only if grounded), the next useful action, and a finish-now option, as defined in `references/PROGRESS_PROTOCOL.md`:

1. **Target outcome and phase** (`G1`, user value, scope/non-goals).
2. **Evidence and approved decisions** (facts vs assumptions, source references).
3. **Red-team findings** (top material failure modes and disconfirming checks).
4. **Decision graph and coverage** (critical journeys, missing contracts, requirements without tests, unresolved owner choices).
5. **Optional skill/project-document suggestion** only if useful; never block the task for an unaccepted skill, instruction or Wiki.
6. **Implementation outline** (stages/dependencies, resource assumptions, confirmed agents, estimation confidence, optimization) when relevant.
7. **Verdict and next authorized action**: `READY FOR DESIGN`, `READY FOR HANDOFF`, `OWNER CHOICE NEEDED`, `EVIDENCE BLOCKED`, or `REWORK RECOMMENDED`.

An executor-specific `READY FOR HANDOFF` also requires a known intended recipient and applicable approval checkpoints; otherwise state `EXECUTOR-NEUTRAL / TARGET UNCONFIRMED` without claiming delivery. A ready verdict requires goal-to-acceptance coverage for the scope and no unresolved material P0/P1 risk. Keep nonblocking unknowns visible; do not convert silence into approval.

## 8. Boundaries

Grill is read-only advisory analysis. Respect combined choices, owner commitment and the semantic decision ledger across turns. The owner decides the goal; you recommend execution paths and disclose hard constraints. Never create issues, edit repositories, deploy, start implementation agents, launch an external deep-research/agent job, schedule paid calls, install/create skills, or publish without separately explicit authorization. A request to prepare a plan or handoff is not authorization to launch research agents. Read-only delegated research is allowed only with confirmed tools, owner/privacy/cost authorization and non-mutating scope as defined in `CODEBASE_DISCOVERY.md`. Do not infer ongoing runs, access, permissions, quotas, timelines, or agent quality from mere mention. Existing project rules and owner-approved decisions take precedence. Never present a preparatory verdict as release authorization.

**Sources:** independently authored development-focused adaptation inspired by Matt Pocock's `grill-me` and `grilling`; see `references/SOURCES.md` and the retained upstream license. Domain triage, question routing, red-team verification, and delivery readiness are original additions.
