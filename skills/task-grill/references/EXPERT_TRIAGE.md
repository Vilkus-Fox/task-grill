# Expert Triage for App, Web, and Game Development

Goal: derive specific questions from an evidence-backed technical and product hypothesis, not from a generic feature checklist. Offer concrete solution options early. Recognize an owner's intent to implement and stop redundant value-proposition debates. This file supplies investigation lenses, **not questions to ask mechanically**.

## First determine the decision surface

- Identify the user's actual job-to-be-done or player's intended experience and the smallest observable success scenario.
- Identify whether the task is exploratory, a feature design, architecture change, bug fix, optimization, or handoff. A bug fix with a proven cause rarely needs a fresh product interview.
- Separate factual constraints, approved requirements, hypotheses, owner-controlled decisions, and reversible implementation details.
- Map a candidate path to the outcome. State what would have to be true for it to work.
- Prioritize investigation by severity of failure, scope of downstream impact, irreversibility, and existing uncertainty. Do not ask every domain question.

## Web products: applicable expert checks

- Primary job and navigation: first-screen utility, meaningful actions, progressive disclosure, keyboard and screen-reader behavior.
- Authentication/authorization boundaries, roles, consent, privacy, data retention; server-side enforcement rather than UI-only access control.
- API and data contracts: source of truth, units, denominators, timezones, data freshness, filtering before aggregation, empty/error states.
- Mobile input and viewport, loading behavior, bundle/runtime performance, caching, offline requirements if applicable, accessibility.
- Existing framework/design system/reuse, compatibility/migrations, deployment platform, production checks and rollback.

## Applications: applicable expert checks

- Platform and supported devices, installation/update, capabilities, permissions, connectivity, persistence, account and synchronization assumptions.
- Core user workflow including interruptions, failed network, unavailable resources, recovery and upgrade/migration.
- Data ownership and transformations, boundaries with APIs/storage, privacy, authentication and accessibility.
- Device-specific CPU/GPU/memory/battery limits and realistic test targets; build and release channels.

## Games: applicable expert checks

- The intended **core loop**: player action, world response, feedback, progression and a minimum playable slice. Distinguish a visual demo from a playable game.
- Engine/platform, control model, input devices, camera, physics, streaming, saves, deterministic requirements, networking, if relevant.
- Progression and economy/balance assumptions, pacing, content pipeline, asset format, licensing, attribution, animation, UI and performance on low-end targets.
- Testable fun hypothesis: what feedback or gameplay evidence could disprove that a mechanic is useful? No invented assurance that a mechanic will be engaging.
- Asset generation versus licensed packs; avoid assuming free equals commercial-use compatible.

## Evidence-first existing codebase checks

When a repository is relevant and accessible, inspect it using `CODEBASE_DISCOVERY.md` *before* asking the owner to describe code the system can read. Code research may be done directly or delegated to explicitly available bounded **read-only** research workers; this is distinct from authorizing coding agents. Record evidence for components, API contracts, tests, repo-local skills and actual environment capabilities.

## Multi-agent development: applicable expert checks

- Agent participation is optional, not a default feature. Confirm inclusion only when it changes the execution plan.
- Distinguish roles: product/UX analysis, repository implementation, visual prototyping, QA/review, integration. Do not invent specific agent availability.
- Check tool/repo access, scope of data that may be shared, local/cloud environment, quotas, paid actions, context limits, and conflict risk only for the selected agent strategy.
- Prefer a single agent plus review when parallelism adds more integration cost than speed; use independent agents only for genuinely separable work.

## What counts as an expert-derived question

A question is justified only if it can name: (1) a concrete goal or requirement ID; (2) the missing owner decision; (3) two substantially different outcomes or paths; (4) cost/risk of deciding wrongly; (5) why evidence cannot settle it. If any item is missing, investigate, make a reversible assumption, or omit the question.

Example: do not ask "What analytics do you want?" when the real risk is that a comparison across flights with different passenger counts needs a valid normalization denominator. Ask which decision the comparison must support, show the denominator options grounded in available data, and explain the semantic risk.
