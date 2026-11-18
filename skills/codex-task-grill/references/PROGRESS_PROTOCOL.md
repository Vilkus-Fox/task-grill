# Honest, Visible Progress and Predictable Exit

## Purpose

Give the owner a clear sense of *where the planning session is going*, what remains, and how to finish now. A progress bar is not decoration, a countdown clock, a probability of success, or a proxy for how many questions were answered.

## Establish the planning frame early

At the beginning, identify the current bounded planning deliverable (e.g. `define first playable slice`, `prepare design handoff`, or `validate an existing feature request`). Select only applicable checkpoints:

1. **Outcome**: desired result, success signal, current-phase boundaries.
2. **Paths**: reasonable solution options and recommendation, using evidence.
3. **Decisions**: essential owner decisions resolved, assumed, or explicitly deferred.
4. **Risk proof**: material red-team risks bounded, disproved or assigned a specific probe.
5. **Delivery**: minimum vertical slice, dependency order and actionable next step.

Do not silently change the denominator. If a new scope is proposed, put it in a later-phase backlog or visibly request a new planning frame rather than repeatedly resetting a near-finished progress bar. If the current phase does not need a checkpoint, omit it at the start. Reopen a completed checkpoint only when new material evidence warrants it and state why.

## Progress representation

Apply `RELIABILITY_PROTOCOL.md`: planning and execution are separate. Show verified execution progress only when the work items and observation source are explicit. A document being created does not prove an installation succeeded, and a plan being completed does not imply code was changed. In the absence of execution evidence, show `Execution: NOT VERIFIED` rather than an optimistic percentage.


- **Planning progress** = `completed applicable checkpoints / applicable checkpoints`. The number is an account of *this bounded planning session*, NOT percent of software built, feature completeness, elapsed time, or guarantee of same-day completion.
- **Decision state** = grounded counts: essential owner decisions still unresolved, evidence checks pending, blocking P0/P1 risks. These numbers are separate from the progress percentage.
- Show the progress **at the beginning**, after each substantive decision or evidence discovery, and in the final synthesis. Do not repeat it after every trivial exchange.
- Display a real graphical progress bar if the host supports it; otherwise use a simple visible text bar such as `Planning [####------] 2/5 (40%)`. Keep the same scale and clearly label it as planning progress.
- Include the current checkpoint, next action, and a **finish-now path**: `Proceed with my recommendation`, `Defer nonblocking choices`, `Close with an interim plan`, or `Pause with blockers`.
- Never invent time-to-finish predictions, remaining question counts, percentages of unknown work, API quota totals, or certainty. If a remaining decision cannot be counted reliably, report `unknown until evidence check` instead of fabricating a number.

## Exit logic

When all applicable checkpoints close, finish with a coherent plan and verdict. If a critical fact remains inaccessible, close the interview with `EVIDENCE BLOCKED`, a bounded test, and any safe work that can continue. If the owner requests a stop, provide an interim decision log and next steps. Do not turn a blocked or paused state into a fabricated `READY` verdict.

## Sample (illustrative, not measured)

`Planning [######----] 3/5 (60%) | Current: risk proof | Owner decisions: 1 | Evidence checks: 1 | Blocking risks: 0`

`Next: confirm storage destination or accept the recommended repository setup. You can also choose 'use recommendation and finish'.`
