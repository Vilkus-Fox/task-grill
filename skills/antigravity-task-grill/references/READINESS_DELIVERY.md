# Outcome Coverage, Staged Delivery and Readiness

## 0. Contract the actual output

Before proposing readiness, record `DELIVERABLE` and `FORMAT` and define output-specific acceptance according to `RELIABILITY_PROTOCOL.md`. A ready-to-execute plan is not a verified installed system. A correct conversation is not a substitute for a requested DOCX, source change or repository handoff.

## 1. Use phase-relative completeness, not arbitrary percentages

**Important distinction:** the user-facing progress bar from `PROGRESS_PROTOCOL.md` measures bounded **planning checkpoints**. It must not be represented as requirements completeness, time-to-finish, percentage of implementation, or measured confidence. Report verified coverage counts and outstanding risk separately.

The objective is not to fill a universal checklist. A task is well-defined when the **minimal intended user/player outcome can be achieved and tested within its chosen scope**, and credible material failure paths have been addressed.

Distinguish phases:
- `CONCEPT`: problem, affected user/player, desired behavior, differentiating benefit, must-not-build constraints and a cheap test of value.
- `DESIGN`: main/negative/edge user paths, semantic contracts, relevant UX/architecture/security/performance choices, measurable acceptance, material risks.
- `HANDOFF`: implementation-grade requirements, owned work packages, tested dependencies, available execution resources and review/integration plan. For executor-specific briefs, the **owner-selected executor/environment** and any independent-agent evaluation or visual-preview approval gate must be preserved. An executor-neutral draft may be ready without selecting an agent, but must be labeled as such.

Define a compact traceability graph with these nodes:
- `G`: observable goal / player outcome.
- `C`: capability, workflow or gameplay loop supporting that goal.
- `R`: scoped requirement and constraint.
- `D`: owner-approved consequential decision, if needed.
- `A`: independently verifiable acceptance check, including failure and boundary paths when material.
- `E`: evidence for a factual claim or feasibility assumption.
- `W`: work package and dependencies for staged implementation.

Essential checks: every must-have `G` has at least one end-to-end `C/A`; every in-scope `R` has an acceptance check; every consequential `D` is reflected downstream; every `W` maps to `R/A`; no work is orphaned; the MVP is an actual user/player journey, not disconnected modules.

Report measurable **counts** where grounded: number of must-have scenarios verified/total enumerated; requirements with/without checks; material unresolved P0/P1 risks; orphan work packages; factually unverified constraints. If the denominator is unknown or scope unbounded, say so and avoid a misleading 100%. Thematic lenses (outcome, scope, data, UX, acceptance, architecture, dependencies, resources) are diagnostic, not equal-weight votes.

Readiness verdict is a reasoned gate, not a calculated probability:
- `READY FOR DESIGN`: concept choices sufficient to design.
- `READY FOR HANDOFF`: scoped requirements and acceptance are traceable, material P0/P1 risks resolved or conclusively bounded, executable work plan is supported; executor-specific readiness cannot be claimed for an unchosen agent, and a requested design-review gate cannot be skipped.
- `OWNER CHOICE NEEDED`: a value/scope/irreversible tradeoff still matters.
- `EVIDENCE BLOCKED`: a crucial factual uncertainty requires research/prototype access.
- `REWORK RECOMMENDED`: evidence conflicts with the plan's principal premise.

An interview can stop with a non-ready verdict. An unknown quota blocks only the stage that depends on that quota; it need not block all product design.

## Skill portfolio is derived, not prescribed

For substantial DESIGN/HANDOFF work, read `SKILL_PORTFOLIO.md` after the requirements and repository evidence are understood. Count **actual reusable skills**, not agents or work packages. Give owner a Lean/Recommended/Expanded choice only when variants materially differ; otherwise recommend a single minimal portfolio. Avoid creating a new skill for a one-off task or inventing installed tools. Link each proposed skill to work packages and acceptance evidence.

## 2. Decompose by useful vertical slices

For consequential or multi-stage work, propose a DAG of work packages:

| Field | Required meaning |
|---|---|
| `W` | Short work package ID, outcome and relevant `G/R/A` IDs |
| Inputs | Required upstream contract, approved decision and evidence |
| Deliverable | Observable functionality or artifact, not vague "work on frontend" |
| Dependencies | True blockers and possible parallel packages |
| Acceptance | Test, demo or check proving the package works |
| Responsible role | Confirmed agent or human role, no invented availability |
| Integration | Who joins parts and checks conflicts |
| Risk | Main technical or product uncertainty and cheap early probe |

Prefer a small end-to-end slice that can be reviewed independently. Distinguish a product prototype from production-grade architecture. Do not split work so finely that orchestration costs exceed implementation benefits.

## 3. Estimate effort and real constraints

- Estimate **effort** (work amount) and **elapsed time** (critical path, handoffs, integration, review) separately.
- Use similar completed tasks, codebase size/complexity, actual available implementation/test tools and scope to justify a range. No evidence -> `UNESTIMATED`, with a bounded spike to gather the missing baseline.
- Track only verified agent access, environment permissions, quotas, context limits, credits, external API budgets, project-specific restrictions, and reviewer capacity. State unknowns as `UNKNOWN` and identify their impact.
- Cloud agent involvement is conditional: if owner says **NO**, exclude its dependencies, quotas, security questions and agent allocation; if **YES**, perform a minimal capability inventory, then isolate unverified claims into a testable investigation.
- Parallel work is allowed only if contracts are stable and ownership does not overlap; account for reconciliation, integration and independent review. Never treat maximum agent count as optimum throughput.
- Offer a low-cost baseline and one meaningful optimization: reuse, simpler architecture, reduced scope, prebuilt permitted assets, early performance test, smaller concurrency, or safer staged delivery. Explain quality/risk tradeoffs.

## 4. Handoff boundaries

Grill provides a decision-complete **proposal**. A separately authorized specification and execution process decides what to create, who to assign, and when to merge/release. Do not silently create tasks or start agents, even when all checks pass.

## 5. Final synthesis template

1. **Outcome / scope:** who needs what, why, and what is excluded.
2. **Evidence and decisions:** verified, approved, assumed, missing.
3. **Top red-team challenges:** only material failures and fastest proof/mitigation.
4. **Coverage:** must-have scenarios and acceptance IDs, untested or orphan work counts, remaining P0/P1.
5. **Delivery path:** MVP vertical slice, stages/dependencies, confident or unknown estimates, confirmed agent roles, limitations, optimization.
6. **Verdict:** chosen readiness status with minimum next owner decision or evidence-gathering step.

For a straightforward matter, compress the output; do not require a document for its own sake.
