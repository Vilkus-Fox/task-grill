# Optional Skill and Project Knowledge Recommendations

Use for nontrivial `DESIGN`/`HANDOFF` tasks when reusable expertise or project knowledge may improve the next step. **This is advice, not a mandatory staffing, skill-installation, or documentation gate.** Completing the core task always takes priority. A valid result is `0 skills suggested`, `0 new skills`, `no new Wiki`, or a single existing project instruction.

## 1. Keep skills, agents, tools and documentation distinct

- **Skill:** reusable instructions for a recurring workflow. A skill is not a running worker.
- **Agent:** human/model execution instance. Agent count follows actual independent work and verified capacity, not skill count.
- **Tool:** repository connector, file viewer, browser, test runner or other authorized capability; its presence must be verified.
- **Project instructions / Wiki:** project-specific knowledge (e.g. `AGENTS.md`, contribution guide, architecture note, existing repository Wiki), often more appropriate than a transferable skill.
- **Task specification:** sufficient for a one-off, scoped change; does not require a new skill or Wiki.

## 2. Make suggestions opportunistically, not an interview

1. Establish task scope and inspect available repository and installed-skill facts when access exists. Do not demand a skill catalog or halt progress to inventory tools.
2. If a **relevant existing skill is VERIFIED**, gently mention it once with its exact verified name, what it helps with, and its optional use. The owner may have forgotten it. Do not silently activate a new workflow merely because it exists.
3. If relevant capability is **not installed or cannot be verified**, do not invent an installed skill. Select the lightest useful alternative, if any:
   - One-off task: include instructions and acceptance checks in the task handoff; no extra artifact.
   - Recurring project-specific practice: optionally propose a short project instruction, `AGENTS.md` addition, README/architecture note, or Wiki page **using the existing source of truth**.
   - Repeatable across multiple projects with stable specialist procedure: optionally propose creating/adapting a reusable skill.
4. Offer a proposed new skill or document only when the *concrete benefit* outweighs creation and maintenance cost. Explain the purpose, reuse trigger and minimum acceptance proof in one sentence. Never make creation/install/use a prerequisite for readiness if the task can proceed without it.
5. Honor `NO`, `not now`, `do it without skills`, or an explicit preference for simple instructions as a closed optional branch. Do not re-ask in different words or put it into the blocking issue count unless a new owner-approved scope reopens it.
6. Do not create skills, repository documentation, Wiki pages, agents, or issues in read-only Grill. A separate explicit authorization and appropriate tool/workflow are needed to perform any of these actions.

## 3. Optional recommendation format

For a meaningful gap, keep output under three concise items, e.g.:

`Available: task-specific reviewer skill (VERIFIED). Optional use: inspect PR risk before merge.`
`Missing: repeatable release checklist (PROPOSED). Preferred home: existing AGENTS.md/README; create a new skill only if multiple projects repeat the process.`
`No extra skill/Wiki required: issue + acceptance tests are sufficient.`

When the owner requests a skill portfolio or staffing design, show Lean / Recommended / Expanded **only if the variants alter implementation decisions**. Count verified existing, proposed, and new skills separately, with `UNVERIFIED` when inventory is unavailable. Do not manufacture precise installed counts or count the current Task Grill skill. Never frame a catalog as a required purchase or prerequisite.

## 4. Coordination and handoff

Use `COLLABORATION_HANDOFF.md` when transferring work between ChatGPT Task Grill and Codex Task Grill. A suggestion stays a *suggestion* in the handoff until the owner approves it. Keep skill use, project docs and agent deployment independent decisions. The handoff is valid with an empty skills section. If an existing Wiki/README already covers the area, prefer linking it over creating a duplicate source of truth.

## Example: narrow change in a documented website

Evidence: existing React feature and tests accessible. The owner wants a new comparison button.
- Continue with the ordinary issue/acceptance tests: **no new skill required**.
- If an actually installed code-review or analytics-semantic skill fits, briefly remind the owner it can be used for verification.
- If repeated comparison metrics need stable definitions and project documentation is missing, optionally suggest one short Wiki or README note. If the owner declines, do not block development.

This example is illustrative, not a claim that any particular repository or skill is accessible.
