# Source-of-Truth, Repository and Commitment Routing

## Purpose

Decide early where project decisions and source code belong, without making repository setup a prerequisite for discussing an idea. Recognize a committed builder and shorten the route to the first working result. Do not treat commitment as proof of technical feasibility or as authorization to perform external side effects.

## Repository decision, once

1. If an existing repository has been identified, confirm it from available context/tools and use it as the source of truth. Do not ask 'GitHub or GitLab?' again or create duplicates.
2. If this is a new, seriously intended software project and no repository is known, offer a compact choice early: `A Existing repository`; `B GitHub`; `C GitLab`; `D local/provisional, decide later`. Allow `Both` only as an explicitly managed mirror strategy, not an accidental dual source of truth. Recommend the option that fits confirmed existing team tooling rather than arbitrarily favoring one platform.
3. If the owner does not want a repo yet, close the repo question for the present phase. Retain a decision summary in the current conversation and identify it as provisional, not permanently saved.
4. If a target platform is selected, propose a sensible repository name, privacy default (private until the owner approves public release), minimal starter content, and a single next action. Ask authorization only when it is time to perform repository creation. Do not repeatedly re-confirm the same authorization.
5. Repository creation, writing Issues/files, changing remotes, mirroring, assigning agents, and publishing are **mutating actions**. Grill stays advisory/read-only; hand the action to a separately authorized execution flow with actual connector or CLI support. If GitLab access is unavailable, state that limitation rather than pretending the platform was created.

## Store outcomes, not transcripts

For a created repository, recommend a lightweight set of linked project records where it adds value:

- `docs/planning/DECISIONS.md`: unique semantic decision IDs, accepted options (including combinations), date/context, rationale and reopening trigger.
- `docs/planning/PLAN.md`: final goal, non-goals, staged vertical slices, dependencies, owner/agent responsibilities, confirmed constraints and integration/review.
- `docs/planning/ACCEPTANCE.md`: requirements and demonstrable pass/fail checks; omit empty boilerplate.

Use project conventions or existing issues/specs instead of imposing duplicate files. Keep the real repository and issue tracker as primary source of truth; never infer it is synchronized merely from a chat response. Record only facts the user authorized to store.

## Committed owner signal

An explicit desire to build, test, deploy, or create a repository means `INTENT = COMMITTED` for the current project. Stop repeating 'should you build this at all?' questions. Keep targeted red-team checks of feasibility, safety and costs, but translate findings into a proof-of-concept, engineering trade-off or mitigation, not rhetorical pressure to abandon the goal.

If an idea violates a hard constraint or is demonstrably infeasible, describe the narrow blocker and propose a variant that still serves the owner's intent; never hide material risks. Always distinguish a serious project choice from permission to spend money, use external services, or publish.
