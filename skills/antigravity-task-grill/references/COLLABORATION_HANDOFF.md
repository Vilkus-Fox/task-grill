# Collaboration Handoff: ChatGPT Task Grill <-> Codex Task Grill

Use this reference **only** for material cross-environment planning or a requested handoff. Each Task Grill works independently if the other is not available. A handoff is an evidence-preserving exchange, not a second complete interview, agent launch, repository edit or mandatory document.

## 1. Different responsibilities, one task

- **ChatGPT Task Grill:** establish owner outcome, product/UX/game choices, deliverable/format, scoped requirements, accepted decisions, value and owner-facing tradeoffs.
- **Codex Task Grill:** investigate the actual repository, branch/HEAD, code paths, contracts and tests; challenge technical feasibility; return *new* evidence, contradictions, and smallest next bounded technical step.
- Both may work alone. When both work on the same task, reuse the previous accepted reasoning and report **delta only**. Repeat red-team only where new evidence affects a material risk. Do not run two full planning interviews by default.
- Never imply an active agent-to-agent connection unless tools actually moved the handoff. Where tools are absent, provide a concise ready-to-paste packet for the user.

## 2. Minimal handoff packet

Carry just the information necessary to continue. Use a Markdown note (or a short in-chat block) with the following conceptual fields; a machine-readable file is **optional**, not an additional requirement:

```yaml
handoff_version: 1
task_id: "FEATURE-EXAMPLE"       # stable within this task
scope: "One sentence of the agreed change"
from_role: "chatgpt-task-grill"   # or codex-task-grill
to_role: "codex-task-grill"       # or chatgpt-task-grill
phase: "DESIGN"                  # CONCEPT | DESIGN | HANDOFF
outcome: "User-observable end result"
deliverable: "Requested artifact and format"
execution_target: "UNCONFIRMED"  # selected implementer/runtime, if known
evaluation_intent: "UNKNOWN"   # DIRECTED_DELIVERY | INDEPENDENT_AGENT_TEST | UNKNOWN
approval_gate: "NONE"       # e.g. visual preview before authorized implementation
sharing_mode: "NORMAL"     # NORMAL | BLIND_FIRST for autonomous-agent comparison
repository: "UNKNOWN"           # exact repo when verified
base_sha: "UNKNOWN"             # exact inspected commit when verified
approved_decisions:              # stable IDs; no reinterpretation
  - {id: "D1", value: "Both running and defense modes"}
verified_evidence: []            # path:line/SHA/tool citations and verifying runtime
receiver_unverified: []           # cannot re-check here != never verified
unknown_evidence: []
material_open_gates: []          # owner decisions or evidence needed
risk_delta: []                  # new or changed material risks
work_packages: []
optional_suggestions: []        # skill/Wiki/project instructions; may be empty
acceptance_checks: []
next_actor: "codex-task-grill"
next_action: "Inspect bounded code paths and return evidence delta"
```

Executor/evaluation/approval fields are conditional, never mandatory paperwork for a small request. Do not force the full schema into short conversations. Exclude irrelevant sections. Record explicitly when `repository`, `SHA`, installed skills or results cannot be verified. No fabricated paths, owners, progress or test successes.

## 3. Handoff rules and decision authority

1. **Owner-approved choices stay closed.** The receiving role must not re-ask or silently replace them.
2. **Retrieve facts first.** Codex reads available code and tests; ChatGPT uses the verified evidence rather than making the owner describe retrievable implementation details.
3. **Return a delta:** added/changed repo evidence, exact contradictions, affected requirement/decision IDs, and the cheapest falsification or acceptance check. Unchanged decisions do not need restatement.
4. **Reopen a decision only** if grounded P0/P1 evidence materially contradicts it. Explain the conflict and propose options. Nonblocking P2 details remain defaults.
5. **Respect permissions:** read-only Grill may output a handoff text or separately requested standalone artifact, but must not write to a repository, launch implementation agents, install skills or change Wiki pages without separate authorization.
6. **Suggestions are not gates:** skill reuse, skill creation, AGENTS.md/README/Wiki authoring, and optional tools stay opt-in. Owner refusal prunes this optional branch; keep the core path open.
7. **Deduplicate:** if the recipient already has the latest task evidence or a previous packet, send only the new evidence and changed IDs. Do not silently change planning scope or denominator.
8. **Select the actual executor:** never infer Codex is the implementer just because Codex reviewed the repository. If the target is unknown, offer an executor-neutral handoff and state what is unresolved.
9. **Respect independent-agent evaluation:** a blind-first prompt shares approved goals, boundaries and tests but not internal code-location hints or previous expert answers. Keep owner-facing private evaluation evidence separate; request approval before moving from prototype to implementation.
10. **Preserve provenance across access gaps:** if the recipient cannot access a private repo, keep **tool-verified, trusted provenance** facts labeled `VERIFIED_BY_SENDER / NOT_REVERIFIED_BY_RECIPIENT`, with source and exact SHA, rather than rewriting them as globally unknown. Do not leak private evidence to an unauthorized service, and revalidate freshness before edits.

## 4. Return packet from Codex to ChatGPT

Use this terse structure when an owner choice is genuinely needed:

`Verified: [path:line, SHA, relevant contract/tests]`
`New finding: [technical constraint and affected R/D ID]`
`Impact: [P0/P1 failure, why it blocks or changes approach]`
`Recommended resolution: [default, compatible options, smallest test]`
`Unchanged approvals: [IDs preserved]`
`Optional suggestions: [none or one relevant skill/document]`
`Next: [owner decision or ready-to-hand-off action]`

If no material contradiction is found, return `No owner choice needed` and the minimum evidence-backed handoff. Do not invent a blocker to create another interview.

## 5. Stop and fallback

For a small fix, a single agent or ordinary task instruction is usually enough. If a handoff recipient is unavailable, no transmission channel exists, or the owner wants to proceed immediately, provide a bounded standalone specification with `NOT VERIFIED` where relevant, without demanding cross-runtime coordination. Do not publish, create external docs, or change files to make the process look complete.
