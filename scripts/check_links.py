#!/usr/bin/env python3
"""Check that every relative Markdown link/image in the repo resolves to a file.
Usage: python3 scripts/check_links.py   (exit 0 = OK, 1 = broken links)
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LINK = re.compile(r'!?\[[^\]]*\]\(([^)\s]+)\)')
broken = 0
for dp, _, files in os.walk(ROOT):
    if '/.git' in dp:
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        path = os.path.join(dp, f)
        text = open(path, encoding='utf-8').read()
        text = re.sub(r'```.*?```', '', text, flags=re.S)  # ignore fenced code blocks
        text = re.sub(r'`[^`\n]*`', '', text)                # ignore inline code
        for target in LINK.findall(text):
            if target.startswith(('http://', 'https://', 'mailto:', '#')):
                continue
            target = target.split('#')[0]
            if not target:
                continue
            full = os.path.normpath(os.path.join(dp, target))
            if not os.path.exists(full):
                broken += 1
                print(f'BROKEN  {os.path.relpath(path, ROOT)} -> {target}')
print('OK: all links resolve' if not broken else f'{broken} broken link(s)')
sys.exit(1 if broken else 0)
