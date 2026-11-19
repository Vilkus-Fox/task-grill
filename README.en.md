# Task Grill 1.6.1 Preview · Development Task Preflight

[Русский](README.ru.md) · [Changelog](CHANGELOG.en.md) · [Home](README.md)

## Purpose

**Task Grill** helps owners of applications, websites, and games clarify consequential requirements **before implementation**. It examines available evidence, proposes concrete options, challenges engineering risks, and prepares a bounded, verifiable handoff. The goal is fewer costly iterations, not more questions.

This is an **advisory Skill**, not an autonomous coding agent. It does not authorize modifying repositories, starting agents, merging PRs, or deploying a project.

## Three standalone skills

| Skill | Environment | Role |
| --- | --- | --- |
| [task-grill](skills/task-grill/SKILL.md) | ChatGPT | Product outcomes, UX, requirements, owner decisions, risks, handoff |
| [codex-task-grill](skills/codex-task-grill/SKILL.md) | Codex | Repository-backed code/test inspection, architecture risks, readiness review |
| [antigravity-task-grill](skills/antigravity-task-grill/SKILL.md) | Google Antigravity | Workspace-based evidence inspection, risk challenge and bounded read-only handoff |

All three Skills can operate independently. For combined work, they exchange **material deltas only**, avoiding duplicate interviews. Canonical references live in [shared/references](shared/references); each standalone Skill contains its own reference copies.

## Getting started

1. Install the appropriate Skill in your environment. In ChatGPT, open your Skills library (`/skills`) and import a ZIP containing **one Skill only**. For Codex, place the Skill directory according to your installed Codex environment's instructions. For Google Antigravity, copy the whole `skills/antigravity-task-grill` folder to `<workspace-root>/.agents/skills/antigravity-task-grill/` and invoke `/antigravity-task-grill` in the App (see [official docs](https://antigravity.google/docs/skills)); no global installation is needed. Do not bundle multiple Skills into one import ZIP.
2. Describe your task naturally, for example: “Grill this homepage redesign; first inspect the repository constraints. Do not make changes yet.”
3. Specify the target executor, independent AI-agent evaluation intent, or required visual approval if these matter. The Skill should recover already-approved decisions and ask only material unresolved questions.
4. Review the result: **goal, verified evidence, outstanding owner decisions, risks, acceptance checks, bounded work packages, and the next authorized action**.
5. Authorize implementation, issue/PR changes, or deployment **separately**, outside advisory Grill mode.

When evidence is unavailable, the Skill must distinguish verified facts from assumptions. A recipient agent lacking private repository access does not erase earlier verified evidence; preserve provenance, SHA, and re-verification status.

## Depth of analysis

- **QUICK:** a small clear bug; full grilling is usually unnecessary.
- **DESIGN:** choices involving UX, product behavior, or architecture.
- **HANDOFF:** acceptance-backed requirements for an approved executor, or an explicitly executor-neutral packet.

These are descriptive modes, **not dedicated UI controls**. Additional Skills are optional, including **zero** additional Skills.

## Independent-agent evaluation

If an owner wants to assess another agent such as Antigravity, an initial blind-first brief contains goals, constraints, and acceptance criteria, **not the coordinator's file-by-file solution or prior audit**. For consequential visual changes, demonstrate a reviewable prototype before seeking authorization to implement.

## Validation and limitations

[SCENARIO_TESTS.md](shared/references/SCENARIO_TESTS.md) describes **57 expected behavior scenarios**; [EVALUATION_GUIDE.md](tests/EVALUATION_GUIDE.md) gives the evaluation protocol.

- **PASS:** static structure tests and integrity of three standalone skill packages.
- **NOT RUN:** systematic live-model behavioral tests and comparisons against upstream Grill Me.
- **Important:** writing 57 test scenarios is **not** the same as passing 57 executed model tests.

Run from the repository root:

```sh
python tests/STATIC_VALIDATION.py
python tests/HANDOFF_STRUCTURE_TEST.py
python scripts/sync_shared.py
```

The last command refreshes copied references inside the three Skills; run it **only when intentionally synchronizing source changes**.

## Packaging

For ChatGPT, package **only** the `skills/task-grill` directory so the ZIP contains `task-grill/SKILL.md`. For Codex, package `skills/codex-task-grill` similarly. For Antigravity copy or package the complete `skills/antigravity-task-grill` folder, including `references/`; no OpenAI UI metadata is required. Prefer an official environment packager where available. Verify `SKILL.md`, `agents/openai.yaml`, and `references/` before importing.

## License and attribution

Original additions are available under [MIT](LICENSE). Inspired by Matt Pocock's `grill-me` / `grilling`: [upstream project](https://github.com/mattpocock/skills), [attribution](shared/references/SOURCES.md), and [upstream license](shared/references/UPSTREAM_LICENSE.txt).

**Antigravity live pilot: NOT RUN** (requires an actual Antigravity session).

**Version 1.6.1 status:** public preview, not a stable release. Keep frozen 1.6 as the comparison baseline. The 1.6.1 changes arise from the BFDO/Antigravity pilot and still require behavioral validation.
