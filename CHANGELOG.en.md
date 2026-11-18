# Changelog

[Русский](CHANGELOG.ru.md) · [Documentation](README.en.md)

## 1.6.1-preview · November 18, 2026

- Preserve the owner's chosen executor and environment; never silently assign Codex.
- Distinguish regular directed delivery from independent evaluation of another AI agent.
- When no executor is selected, prepare an explicitly **executor-neutral handoff** or ask one material question.
- For substantial visual changes, preserve a reviewable prototype and explicit design-approval gate.
- Do not launch external Deep Research / AI-agent runs merely because a plan or handoff was requested.
- Preserve cross-runtime evidence provenance (source, SHA, verifier), without claiming newly performed checks.
- Keep **G → C → R → A** semantics: Goal → Capability → Requirement → Acceptance.
- Added scenarios T50–T57, **57 scenarios** total.
- **Static validation passed; live-model behavioral tests NOT RUN.**

## 1.6 · Candidate

- Optional suggestions for extra Skills, README/AGENTS.md/Wiki; using zero is valid.
- Compact decision-and-evidence handoff across ChatGPT and Codex without repeating settled questions.
- Added scenarios T38–T49 (49 total).

## 1.5 · Candidate

- Inspect available repository and existing rules before asking material questions.
- Bounded read-only investigation, optional capabilities, context efficiency.
- Added scenarios T28–T37 (37 total).

## 1.4 · Candidate

- Renamed to `task-grill` and `codex-task-grill`, with “Прожарка задачи” display name.
- Added deliverable-format checks and separate planning-versus-execution status.
- Added scenarios T20–T27.

**Note:** scenario counts represent authored evaluation cases, not evidence that models passed them.
