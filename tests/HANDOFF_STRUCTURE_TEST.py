#!/usr/bin/env python3
"""Structural invariants for Task Grill 1.6.1; not a model behavior test."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
refs = root / 'shared' / 'references'
portfolio = (refs / 'SKILL_PORTFOLIO.md').read_text(encoding='utf-8')
handoff = (refs / 'COLLABORATION_HANDOFF.md').read_text(encoding='utf-8')
cases = (refs / 'SCENARIO_TESTS.md').read_text(encoding='utf-8')
assert 'optional' in portfolio.lower()
assert 'Wiki' in portfolio and 'AGENTS.md' in portfolio
assert '0 new skills' in portfolio or 'zero new skills' in portfolio
assert 'read-only' in portfolio
for phrase in ['approved_decisions', 'verified_evidence', 'material_open_gates', 'optional_suggestions', 'owner-approved', 'delta']:
    assert phrase.lower() in handoff.lower(), phrase
for n in range(38, 58):
    assert ('## T%d.' % n) in cases, n
for slug in ['task-grill', 'codex-task-grill']:
    skill = (root / 'skills' / slug / 'SKILL.md').read_text(encoding='utf-8')
    assert 'COLLABORATION_HANDOFF.md' in skill
    assert 'SKILL_PORTFOLIO.md' in skill
    assert 'EXECUTOR-NEUTRAL' in skill, slug
    assert 'approval' in skill.lower(), slug
assert 'execution_target:' in handoff
assert 'evaluation_intent:' in handoff
assert 'BLIND_FIRST' in handoff
assert 'NOT_REVERIFIED_BY_RECIPIENT' in handoff
print('PASS: optional skills/Wiki, delivery routing, and handoff structure (not model evaluation)')
