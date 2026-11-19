# Question Router and Infinite-Interview Protection

**Principle:** Questions are a decision tool, not a completion metric. Follow `DECISION_UX.md` for solution-first recommendations, semantically deduplicated decision IDs and combined choices, and `PROGRESS_PROTOCOL.md` for visible bounded planning progress. Never require a fixed number of rounds and never reward the model for finding more questions.

## 1. Route each unknown to the correct treatment

| Unknown type | Treatment | Example |
|---|---|---|
| `FACT` | Find evidence from permitted source, do not ask owner if accessible | Does the repo already contain a comparison API? |
| `OUTCOME` | Focused open question if the owner has not specified the desired result | What should a player gain from defending instead of running? |
| `GATE` | Closed yes/no, prune the excluded branch | Will cloud agents be involved? |
| `CHOICE` | Recommended alternatives with combined choices when feasible and a freeform escape | Compare absolute plays, normalized plays, or both? |
| `ASSUMPTION` | Choose a reversible low-risk default; label and test | Initial chart range |
| `RISK` | Verify a critical assumption or ask a targeted owner tradeoff | Can viewers access other airlines' aggregate data? |
| `MISSING_EVIDENCE` | Propose a bounded investigation with pass/fail criterion | Agent quota undocumented |
| `LATER` | Record and defer; do not ask now | Cosmetic animation after MVP |

A broad question is valid only when the goal cannot be reconstructed from available context. Prefer a concrete paraphrase and an explicit opportunity to correct it. Do not disguise a multi-part interview as one open question.

## 2. Branch semantics

1. Before asking, record `question_id`, `parent_decision`, `outcome_affected`, `type`, `alternatives`, `recommendation`, `risk_if_wrong` and `downstream_nodes` in the reasoning/work artifact when useful.
2. After a **NO** to an optional feature, mark dependent nodes `NOT_APPLICABLE`. Do not ask child questions, produce an implementation plan for that branch, or count it as a completeness gap. Reopen it only after the owner explicitly changes scope.
3. After a **YES**, expand only the immediate relevant child nodes. First find facts in available documentation, code, account tools, or trusted references; owner questions are reserved for material preferences or access decisions. Do not infer that a YES means authorization to activate agents or buy services.
4. If branch facts are unavailable, state what is unknown, propose the smallest evidence-gathering task and its success criterion, then stop that branch at `EVIDENCE BLOCKED`. Never recursively enumerate all possible unknown infrastructures.
5. If two independent critical choices can be considered together without confusing dependencies, group them; otherwise resolve the parent before the child. If proposed options are compatible, offer BOTH/A+B, not a forced XOR. There is **no fixed per-round question count**.

**Example: cloud agents**
- `Will the plan use cloud agents?` -> **No**: close cloud-agent planning entirely; evaluate only confirmed alternatives and their limits.
- **Yes**: inspect already confirmed providers, access, permissions, data restrictions, quotas, and repository access. Ask only the next consequential owner decision. If provider/capabilities cannot be verified, propose a short capability probe, mark the branch pending, and continue with non-cloud scope where possible.
- **Not decided**: explain the minimal single-agent baseline and the upside/downside of cloud agents; ask for a choice only if execution feasibility depends on it.

## 3. Question priority

Ask only if the answer changes one of: end-user outcome, irreversible contract, feasibility, exposure to P0/P1 risk, material cost/schedule, or MVP scope. Prefer a question that unlocks multiple downstream decisions. A P2 reversible preference should not block handoff.

For every asked question, use a compact structure:
- **Observation:** verified fact or clearly labeled uncertainty.
- **Decision:** one focused open question or bounded choice, directly tied to outcome/requirement.
- **Recommended path:** one recommendation and its tradeoff.
- **What changes:** dependency or risk eliminated by the answer.

Match against the semantic decision ledger before asking: never re-ask an answered or substantially equivalent question unless contradictory material new evidence arises. Do not make the owner research what the agent can inspect.

## 4. Adaptive stop criteria (no round limits)

Stop interviewing when ANY condition applies:

- Critical dependency paths are resolved for the requested phase, and remaining choices are reversible or out of scope. Produce the synthesis and readiness verdict.
- Further owner questions would not change the plan, acceptance outcome, material risk, or next action (low marginal information value).
- The unresolved blocker is missing factual evidence, not an owner preference. Produce `EVIDENCE BLOCKED` and a specific investigation instead of new questions.
- The user declines, defers, or asks to stop. Record exact unresolved consequences and proceed only within safe authorized scope.
- The same issue has been repeated without new evidence. Collapse it into a single blocker and recommendation; never paraphrase it as a fresh question.

Stopping a conversation is not the same as declaring a plan ready. Keep material unresolved risks in the final artifact. If new evidence invalidates an accepted decision, reopen only the affected branch, not the entire interview.
