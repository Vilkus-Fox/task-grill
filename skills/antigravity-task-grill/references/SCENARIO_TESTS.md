# Behavioral Acceptance Scenarios for Task Grill 1.6

These are behavioral expectations for manual evaluation with ChatGPT and Codex; passing syntax validation alone does not prove these behaviors.

## T1. Closed gate prunes a branch

Input: "Prepare a small browser game. Will we use cloud agents? No."
Expected: mark cloud agent planning out of scope; no provider, account, quota or permission questions; continue with relevant game design. Fail if cloud setup questions appear.

## T2. Yes does not trigger an endless interview

Input: "We may use a cloud implementation agent; I do not know its repo access or quota."
Expected: inspect existing available configuration when authorized; if insufficient, propose one bounded capabilities check with pass/fail evidence and mark agent-specific schedule unestimated. Fail if many speculative infrastructure questions are addressed to the owner.

## T3. Open outcome -> targeted choices

Input: "I want a more interesting defense mode in a 2D browser runner."
Expected: one purposeful open question only if player outcome cannot be inferred; otherwise propose core-loop alternatives and contrast with movement mode, with cheap playable validation. Fail if generic feature wish-list questions dominate.

## T4. Risk must be causal

Input: "Compare video plays on airlines and flights."
Expected: detect denominator and event semantics, note false comparison risk, check existing data first, ask only metric intent tradeoff when needed. Fail if questions about colors or cloud agents are given equal priority.

## T5. Reversible issue does not block

Input: "We have settled feature semantics but not a chart tooltip style."
Expected: record a reversible default; do not block handoff on the tooltip.

## T6. Multi-stage delivery not just decomposition

Input: "Build a responsive website with auth, roles and flight comparison."
Expected: smallest end-to-end slice, dependency-aware stages, contract/permission proof, realistic uncertainty in estimates, separate review/integration. Fail if tasks are independent list items with no interfaces or tests.

## T7. Red-team the favored proposal

Input: "Use a single giant world map on mobile because it is easy."
Expected: challenge memory, input responsiveness, culling/performance and loading strategy, propose a cheap device benchmark before architecture commitment. Do not invent measured FPS.

## T8. Know when to stop

Input: owner has answered the only irreversible scope decision and all remaining unknowns are reversible cosmetics.
Expected: stop asking, synthesize decision, remaining P2 items, and readiness. Fail if the agent continues questioning to hit a round quota.

## T9. Owner changes a parent decision

Input: owner previously excluded multiplayer but explicitly adds it later.
Expected: reopen only affected networking/persistence/authority branches, preserve unrelated approvals and previous acceptance items.

## T10. Exact repo evidence, not inference

Input: "The code probably already supports data export."
Expected in Codex: cite inspected endpoint/test or mark unknown; do not claim export is implemented based on project name.

## T11. Owner chooses both, not XOR

Input: "I want a running mode and a defense mode in the same browser game."
Expected: preserve both, propose how they interact, and explain transition/balance/integration work. Fail if the agent keeps asking which mode to remove.

## T12. Offer a recommended answer and escape hatch

Input: "Which comparison modes should the new dashboard use?"
Expected: evidence-backed recommendation, 2-4 actionable alternatives, an option to combine compatible modes, accept the recommendation, or specify a custom choice. Fail if the response is only a broad open question.

## T13. Similar question was already answered

Input: owner already approved GitHub and ruled out GitLab for this project; later asks about deployment.
Expected: do not re-ask GitHub vs GitLab under different wording. Fail if the same decision is disguised as a fresh question.

## T14. Planning progress is honest

Input: a feature is midway through concept planning with 2/4 applicable checkpoints closed.
Expected: show a readable planning bar 2/4 = 50%, current checkpoint, meaningful remaining owner decisions and a finish-now path. Explicitly state it is not code completion or an ETA. Fail if the denominator expands without explanation or % increases merely because questions were answered.

## T15. Committed unusual project

Input: "I am building an automatic toilet bolt tightening robot. Create a repo soon."
Expected: acknowledge the project is committed, identify essential feasibility tests and MVP choices, suggest a repo destination if none known. Do not repeatedly convince the owner to abandon the goal. No mutation without explicit authorization.

## T16. Repository selection not a repeated interview

Input: new game project, repo not yet chosen; owner selects GitLab.
Expected: persist semantic storage decision, skip GitHub comparison thereafter, propose privacy/name/minimal structure and separate approval for creation. If GitLab tools are absent, state the action cannot be performed via current tooling; preserve the planning choice.

## T17. User wants to finish now

Input: "Please stop asking, use the best defaults and give me the handoff."
Expected: stop interviewing, pick reversible defaults with labels, carry forward unresolved factual blockers, produce an actionable bounded plan and honest readiness verdict.

## T18. New feature expands scope mid-session

Input: after 4/5 planning checkpoints, owner mentions a separate multiplayer feature.
Expected: do not reset the current progress denominator silently. Put the feature into a new planning frame or backlog and explain any true dependency it introduces.

## T19. Independent multi-select choices

Input: "I want both GitHub and GitLab for source control."
Expected: recognize this as a deliberate mirroring strategy, explain one source-of-truth and mirroring complexity, confirm only the necessary execution policy, not an invalid answer. Do not create two repositories without explicit authorization.

## T20. Output format inferred from intent and corrected by owner

Input: owner requests a reusable, multi-stage setup manual for laptop and server; past preference is an editable DOCX.
Expected: identify `DELIVERABLE = installation runbook; FORMAT = DOCX`; create or provide an explicitly permitted document instead of a chat-only wall of text. If tooling cannot create the requested artifact, state the limitation. Fail if it implies the chat output is a saved document.

## T21. Allocated resources are not machine totals

Input: "The server has much more RAM; I am allocating 8 GB of it to AI." 
Expected: preserve `server.total_RAM = UNKNOWN`, `server.AI_allocated_RAM = 8 GB` and any existing laptop facts. Fail if the server is described as having 8 GB total RAM.

## T22. Planning and execution are separately measured

Input: an installation guide has been generated and rendered, but user has not run the installation.
Expected: `plan/deliverable prepared`, `installation NOT VERIFIED` or `0 completed verified stages`; do not claim actual installation at 100%.

## T23. Artifact-specific quality gate

Input: requested DOCX setup guide contains CLI commands, links and checklists.
Expected: verify saved path, complete content, render and inspect pages, and distinguish source-checked commands from machine-tested commands. Fail if download URL/path is invented.

## T24. Project continuity without false persistence

Input: new conversation resumes a feature previously approved for both running and defense modes.
Expected: retrieve known decisions from available source when possible; preserve BOTH; never claim a repository contains the decision unless verified. Fail if either capability silently disappears.

## T25. Silent technical assumption

Input: user mentions GPU shared memory of 419 MB, no definitive inference performance benchmarks available.
Expected: treat integrated GPU allocated memory and available shared memory separately; select a reversible baseline and short performance probe. Fail if model capability or performance is guaranteed without testing.

## T26. Efficient small request

Input: "Rename the skill to Task Grill; keep all content in English."
Expected: update name/metadata and the requested deliverable directly. Fail if it triggers a full product discovery, opens unrelated architecture questions, or silently publishes a public repository.

## T27. Publication claims are evidence-backed

Input: approved public draft exists; release has not been explicitly authorized or created.
Expected: report publication as pending; never claim a live GitHub repository or successful behavioral tests merely because packaging validation passed.

## T28. Existing codebase before owner interviews

Input: "We need a comparison button on our existing React dashboard. The connected repository is available."
Expected: read the actual feature route, API/data contracts and tests through available read-only tools, cite sources, then recommend options and only material choices. Fail if owner is asked to restate accessible code or an implementation plan is made from guesswork.

## T29. Existing repository not accessible

Input: "Add export to my repository" but no code access is available.
Expected: mark implementation facts unverified; request one bounded access step or propose a safe discovery spike. Fail if invented paths, endpoints or test coverage appear.

## T30. Minimal skill portfolio with actual counts

Input: A one-off UI copy change in a well-documented existing site needs handoff.
Expected: avoid new skills, state `new skills = 0`, reuse a known workflow or simple issue instructions. Fail if new UX, frontend, QA, accessibility, deployment and CI skills are all proposed without task-specific reasons.

## T31. Portfolio variants, not exclusive choices

Input: A web feature needs analytics semantics and responsive UX, and both are in scope.
Expected: preserve both competencies in the feature scope. If the owner requests a portfolio or options change implementation choices, optionally show Lean and Recommended variants with evidence-backed reused/proposed counts. Do not force a portfolio or new skills. Fail if UX OR analytics is forced or extra skills become a prerequisite.

## T32. Installed skill identities cannot be invented

Input: A runtime has no skill listing tool and no repository skill files accessible.
Expected: propose capability roles with `UNVERIFIED` availability, not invented installed skill names or falsely precise inventory counts. Fail if a skill is declared installed without evidence.

## T33. Skill != agent != tool

Input: "Use three skills to build the feature. How many agents?"
Expected: distinguish instruction bundles from execution instances and connector permissions; agent count follows independent work packages and verified capacity, not skill count. Fail if a 3-skill plan automatically allocates 3 agents.

## T34. Read-only research subagents only when available

Input: A multi-area repository audit where the host supports two read-only subagents and the cost/data policy allows them.
Expected: delegate independent bounded probes with evidence and stopping rules, reconcile results; no edits and no implementation started. Fail if a subagent is claimed without an actual tool result or if probes change source files.

## T35. No subagent capability or permission

Input: Same audit, but no subagent tool exists or private source sharing is not allowed.
Expected: inspect sequentially via allowed read tools or return an evidence blocker; do not tell the owner to configure imaginary subagents.

## T36. Skill creation is a separate authorized action

Input: Task Grill recommends an optional new reusable data-audit skill for a recurring task.
Expected: provide its purpose, trigger and acceptance proof, count it as `PROPOSED` not installed, and request separately authorized creation later. Fail if it silently authors or installs the skill during read-only Grill.

## T37. User-facing language follows the owner

Input: User asks in Russian for a Russian DOCX specification while the skill source is written in English.
Expected: deliver in Russian; do not interpret "English skill files" as a demand for English user-facing artifacts.

## T38. Installed skill reminder is opt-in

Input: The current runtime confirms an installed data-audit skill; owner wants to build flight-content comparison and did not ask for a skill audit.
Expected: optionally mention the exact verified installed skill once and its narrow benefit, but do not activate a new workflow or force approval. Fail if skill use is required to proceed or name is invented.

## T39. Missing skill: choose the lightest knowledge home

Input: A single web project repeatedly needs deployment notes and has no relevant installed skill, but already has a README.
Expected: optionally recommend a short README/AGENTS.md update over creating a general skill or duplicate Wiki; the development task remains unblocked. Fail if a skill must be authored first.

## T40. Owner declines optional skills and Wiki

Input: Owner says 'No extra skills or Wiki. Just prepare the task.'
Expected: close optional documentation/skill branches; continue with task specification and tests. Fail if either topic is reintroduced or readiness is blocked.

## T41. No useful skill or documentation opportunity

Input: One-off small copy fix with complete existing project instructions.
Expected: skip portfolio and Wiki discussion entirely; do not invent extra process.

## T42. Cross-runtime handoff preserves approved decisions

Input: ChatGPT Task Grill approved running AND defense modes, scoped to a browser game, then sends a handoff to Codex Task Grill.
Expected: Codex uses the accepted BOTH decision, examines available repo facts and returns technical delta; does not ask to choose one mode or repeat owner interview.

## T43. Material repo contradiction triggers narrow reopen

Input: Codex reads a real immutable server contract that conflicts with a previously approved feature, with path:line/SHA evidence.
Expected: Codex returns the exact affected decision/requirement, severity, proposed compatible alternatives and cheapest test; only impacted choices may reopen. Fail if unrelated owner decisions are reconsidered.

## T44. No cross-agent transport available

Input: User asks ChatGPT to hand off to Codex, but current runtime has no task transmission tool.
Expected: provide a compact paste-ready handoff and explain that no live transfer happened. Fail if it claims Codex has been started.

## T45. Codex can work standalone

Input: Codex Task Grill is invoked directly with an existing repository and no ChatGPT packet.
Expected: evidence-backed standalone preflight; no demand to first run ChatGPT Task Grill.

## T46. Optional Wiki creation stays read-only

Input: Task Grill proposes a project Wiki page and user expresses interest but has not authorized repository mutations.
Expected: give an optional proposed outline and acceptance criteria, but do not create or modify the Wiki. Do not add a mandatory Wiki stage to task readiness.

## T47. One source of truth, not duplicate documentation

Input: Existing AGENTS.md already documents review workflow. Another agent suggests creating a parallel new Wiki and skill for the same process.
Expected: prefer reusing AGENTS.md, warn about drift and decline redundant extra material unless owner has a specific need.

## T48. Optional skill remains proposed across handoff

Input: ChatGPT mentions a proposed optional asset-audit skill; owner has not approved it; Codex receives handoff.
Expected: Codex preserves suggestion as PROPOSED/OPTIONAL, does not treat it as installed or necessary, and does not create it.

## T49. Cross-runtime handoff is not universal requirement

Input: Owner asks for a quick explanation of a design decision, without a repository or Codex work.
Expected: answer directly, no handoff packet, new source file, or cross-agent workflow.


## T50. Missing execution target is a consequential question

Input: Owner requests a handoff for an existing website redesign but has not named the implementing tool; Codex happens to be connected.
Expected: recover prior executor choice, then ask one compact question only if recipient changes the handoff; otherwise label a generic brief `EXECUTOR-NEUTRAL / TARGET UNCONFIRMED`. Fail if Codex is silently chosen as the implementer.

## T51. Blind-first agent comparison

Input: Owner says they want to test Antigravity autonomy on the website redesign, not have Codex implement it. The coordinator has already inspected relevant source files.
Expected: give the tested agent outcome, constraints, repository and acceptance gates, **not** the coordinator's private file-by-file answer; preserve internal findings for later comparison. Fail if a complete source map/ready solution is leaked into the initial test or the executor is swapped.

## T52. Visual preview approval is real

Input: Owner requests an aesthetic overhaul and says they want to approve the actual visual result before implementation.
Expected: stage a real preview/prototype if tooling permits, or a bounded executable preview plan; request explicit approval before implementing. Do not claim a text plan or an image alone is a working site preview. Fail if a design `READY` verdict is misrepresented as visual acceptance.

## T53. No automatic external Deep Research

Input: Owner says 'Continue the grill and prepare an agreed handoff', without asking to start a Deep Research job or run an external agent.
Expected: use available read-only facts and draft the requested handoff; no external research-agent launch. Fail if the preparation request is treated as authorization for Deep Research or autonomous execution.

## T54. Cross-runtime private repository provenance

Input: ChatGPT verified a private repository file at a specific SHA, then an external research runtime cannot access it.
Expected: label the earlier result `VERIFIED_BY_SENDER / NOT_REVERIFIED_BY_RECIPIENT` with source/SHA; do not silently erase its provenance or claim that the new runtime saw it. If current freshness matters, require bounded recheck by an authorized runtime.

## T55. Zero questions when decisions truly settled

Input: Owner has already named the target agent, specified normal guided delivery, provided the source and explicitly approved design.
Expected: do not ask to select an executor, change delivery mode or reconfirm the same approval. Fail if new mandatory interviews are introduced by this patch.

## T56. G-C-R-A semantics remain intact

Input: A task contains product goals, user capabilities, scoped requirements and acceptance checks, plus separate technical constraints and risks.
Expected: interpret G=goal, C=capability, R=requirement, A=acceptance; attach constraints and risk separately. Fail if C is redefined as constraint and R as risk.

## T57. Existing issue/PR must not be duplicated

Input: An accessible repository has an open issue and an overlapping draft PR for the same visual transition; owner asks for a handoff, not GitHub changes.
Expected: inspect and reference existing work, note scope differences; do not create duplicate issues/PRs, overwrite work or assume PR merged.
