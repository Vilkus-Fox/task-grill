#!/usr/bin/env python3
"""Sync shared reference source into standalone skill directories."""
from pathlib import Path
import shutil
ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'shared' / 'references'
for skill in ['task-grill', 'codex-task-grill', 'antigravity-task-grill']:
    dest = ROOT / 'skills' / skill / 'references'
    dest.mkdir(parents=True, exist_ok=True)
    for src in source.iterdir():
        if src.is_file():
            shutil.copy2(src, dest / src.name)
print('Synced canonical references into all standalone skill directories')
