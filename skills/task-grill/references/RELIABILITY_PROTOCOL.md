# Reliability Protocol: Deliver the Work, Not Just the Discussion

## 1. Outcome contract comes before questions

Before diagnosing a task, derive a concise, testable **outcome contract** from the owner's actual request and existing decisions:
- `G`: what the user/player must be able to do.
- `DELIVERABLE`: the concrete end product, e.g. advice, options, a specification, a DOCX manual, source files, prototype, review, or verified deployment.
- `FORMAT`: user-specified format, or a justified default consistent with the intended use. Do not ask for format if context settles it.
- `ACCEPTANCE`: how the specific deliverable will be checked; do not confuse artifact existence with operational success.
- `BOUNDARY`: what this consultation may produce, and which external side effects require separate owner authorization.
- `EXECUTION_TARGET` (only when handoff/execution is relevant): the owner-selected agent/runtime, or `UNCONFIRMED`. Do not treat a tool that happens to be connected as the selected executor.
- `EVALUATION_INTENT` (only when relevant): normal directed delivery or an independent capability test of a specific agent. These call for different briefs.
- `APPROVAL_GATE`: when to stop for owner review, especially an interactive/visual prototype before substantial aesthetic implementation.

A substantive reusable runbook with commands/checkpoints usually merits a durable editable document if the environment supports that artifact, rather than a long chat-only response. Technical repositories may instead prefer Markdown near the codebase. Use the owner's stated format first. If two materially different formats remain equally likely and choice matters, offer a short recommended choice. Do not fabricate documents or links without creating and verifying them. A skill can recommend delivery; it cannot claim that an independent execution step happened. A request to **prepare** a handoff does not authorize launching an external Deep Research run, paid tool or development agent.

## 2. Facts are typed, scoped and source-backed

Record consequential claims as:
- `USER_CONFIRMED`: an explicit statement from the owner, preserving its qualifiers.
- `VERIFIED`: grounded in accessible docs, inspected code, tool responses, or observed tests, with provenance.
- `ASSUMED`: provisional and reversible, with a specific verification trigger.
- `UNKNOWN`: missing and not safe to infer.

Retain entity and unit: `server.total_RAM` is NOT `server.AI_allocated_RAM`; `GPU.dedicated_VRAM` is NOT `shared_GPU_memory`; repository presence is NOT write access; software installed is NOT software tested. A prior statement, especially one carrying qualifiers like 'allocated', 'estimated', 'planned', or 'might', must never be promoted to a stronger fact.

Before issuing commands on an existing machine or repository, check OS and platform family, target directories, scope of access, resource budget and consequences. If a material fact cannot be read, provide a safe conditional branch and a *single bounded probe* instead of speculative interrogation.

## 3. Deliverable quality and execution evidence are different

Use the acceptance method relevant to the promised output:
- `DOCUMENT`: verify file exists, contains complete instructions, renders cleanly, has copyable commands and clearly labeled platform/privilege boundaries; visual QA for DOCX/PDF.
- `CODE`: inspect diff, build/test/lint where authorized and possible, record exact commands and results. Unrun tests are `NOT RUN`.
- `REPO/PR`: verify repository URL, branch/SHA, diff and actual remote state before claiming changes were published.
- `INSTALL/RUNBOOK`: verify commands against current official documentation when materially time-sensitive; describe reversible checkpoints, diagnostics and rollback. Preparing instructions is NOT a completed installation.
- `DESIGN/PROTOTYPE`: check target-device experience and visible outcome, not mockup count.

When environment execution is out of scope, hand off a precise checklist, not a false pass. A user-visible `100%` planning badge means only planning is done; it never says the user's device or product works.

## 4. Dual progress with a stable denominator

Track **planning** and **execution** separately when execution is requested:
- `PLAN`: completed applicable planning checkpoints / declared relevant checkpoints; fixed when framed; only change with an explicit new scope.
- `EXECUTION`: independently verified checkpoints / agreed implementation checkpoints. Unobserved user actions count as unverified, not completed. Do not assign an implementation percentage when no enumerated execution scope exists; use `NOT STARTED` or `NOT MEASURED`.
- Keep status labels such as `PREPARED`, `NOT RUN`, `VERIFIED`, `BLOCKED` and use clear next action. No fake ETA or 'done' based on the length of a reply.

## 5. Resume, do not restart

Maintain one semantic decision ledger keyed by project, phase, and scope, with `decision ID`, exact approved selection (including BOTH), supporting evidence, dependent branches, approval status, and triggers to reopen. Distinguish conversation-only state from durable repository state.

On continuation: recover the latest approved decisions, recent evidence, outstanding blockers, execution target/evaluation intent if applicable, and last confirmed checkpoint first. Never re-ask a semantically answered question, especially when the owner provides a new fact that refines rather than replaces a decision. When the owner wants an interim deliverable, summarize and deliver rather than reopen the interview.

## 6. Suggest optional skills only when they add value

Read `SKILL_PORTFOLIO.md` for nontrivial planning only when a reusable-skill or project-document suggestion might actually help. Offer verified existing skill reuse once if appropriate; new reusable skill or project instructions/README/Wiki are optional and not required for handoff. The owner can decline them with no impact on core task readiness. Do not infer installed tools or agents from skills, and do not claim delegated read-only work occurred without actual execution evidence.

## 7. Do not turn optional reusable assets into blockers

When a relevant skill already exists and is verified, offer a single lightweight reminder if it helps. A missing skill should not trigger a skill-creation project. If there is a recurring project-specific knowledge gap, optionally suggest using the existing project README, AGENTS.md or Wiki rather than creating a cross-project skill. Do not duplicate established documentation or impose a documentation task where none is needed. A refusal closes the optional branch. Apply `SKILL_PORTFOLIO.md` for details. Use `COLLABORATION_HANDOFF.md` only when a meaningful cross-runtime handoff is needed, and preserve accepted decisions without re-interviewing.

## 8. Keep the workflow proportionate

Use only the reliability checks that could prevent a real error in the current scope. In cross-runtime handoffs, preserve source/commit provenance: evidence VERIFIED by runtime A is not globally UNKNOWN because runtime B lacks access; mark it `VERIFIED_BY_SENDER / NOT_REVERIFIED_BY_RECIPIENT` and require freshness checks before consequential execution. Skip diagrams, scoring, custom files and detailed reports for small tasks. An added rule earns its place only if it prevents an observed failure or improves a verifiable outcome. Correct evident mistakes promptly without spinning up another approval cycle. This is a *planning* skill; do not silently perform external side effects.
