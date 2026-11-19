#!/usr/bin/env python3
"""Static structural check; this never substitutes for live-model behavior tests."""
from pathlib import Path
import re
root = Path(__file__).resolve().parents[1]
source = root / 'shared' / 'references'
required = ['RELIABILITY_PROTOCOL.md', 'CODEBASE_DISCOVERY.md', 'SKILL_PORTFOLIO.md', 'COLLABORATION_HANDOFF.md', 'SCENARIO_TESTS.md']
for x in required:
    assert (source / x).is_file(), f'Canonical source missing {x}'
for slug in ['task-grill', 'codex-task-grill', 'antigravity-task-grill']:
    skill = root / 'skills' / slug
    content = (skill / 'SKILL.md').read_text(encoding='utf-8')
    assert content.startswith('---\nname: ' + slug + '\n')
    assert '1.6.1' in content
    assert 'CODEBASE_DISCOVERY.md' in content
    assert 'SKILL_PORTFOLIO.md' in content
    assert 'COLLABORATION_HANDOFF.md' in content
    cases = (source / 'SCENARIO_TESTS.md').read_text(encoding='utf-8')
    assert all(('T' + str(i) + '.') in cases for i in range(1, 58))
    assert (skill / 'references' / 'UPSTREAM_LICENSE.txt').is_file()
    if slug != 'antigravity-task-grill':
        assert 'display_name: Прожарка задачи' in (skill / 'agents' / 'openai.yaml').read_text(encoding='utf-8')
    for f in source.iterdir():
        if f.is_file():
            assert (skill / 'references' / f.name).read_bytes() == f.read_bytes(), f'Out of sync: {slug}/{f.name}'
    for f in [skill / 'SKILL.md', *((skill / 'references').glob('*.md'))]:
        assert not re.search('[А-Яа-яЁё]', f.read_text(encoding='utf-8')), f'Non-English source: {f}'
    print('PASS static structure and reference parity:', slug)
assert (root / 'LICENSE').is_file()
print('NOTE: live-model behavior NOT RUN')
