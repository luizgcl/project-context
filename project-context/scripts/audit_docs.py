#!/usr/bin/env python3
"""Read-only Markdown checks; semantic decisions remain with the user/agent."""
import argparse
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

IGNORED = {'.git', '.agents', '.codex', '.venv', 'venv', 'node_modules',
           '__pycache__', 'dist', 'build'}
STATES = {
    'RFC': {'Draft', 'In Review', 'Accepted', 'Rejected', 'Withdrawn', 'Superseded'},
    'ADR': {'Proposed', 'Accepted', 'Deprecated', 'Superseded'},
}


def visible_lines(text):
    """Keep line numbers while removing fenced code and inline code."""
    fence = None
    for line in text.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not match[2].strip():
                fence = None
            yield ''
        elif fence:
            yield ''
        else:
            yield re.sub(r'(`+).*?\1', '', line)


def anchors(text):
    found, counts = set(), {}
    # Preserve inline code in headings: its text contributes to the slug.
    for line in visible_lines(re.sub(r'`([^`\n]+)`', r'\1', text)):
        match = re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$', line)
        if not match:
            continue
        title = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', match[1]).lower()
        slug = ''.join(c for c in title if c in ' -_' or unicodedata.category(c)[0] in 'LN')
        slug = slug.replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count + 1
        found.add(slug if not count else f'{slug}-{count}')
    return found


def markdown_files(root):
    # Do not follow directory symlinks or inspect tools' private folders.
    for path in sorted(root.iterdir()):
        if path.is_symlink() or path.name in IGNORED:
            continue
        if path.is_dir():
            yield from markdown_files(path)
        elif path.suffix.lower() == '.md':
            yield path


def audit(root, rfc_dir='docs/rfcs', adr_dir='docs/adrs'):
    root = Path(root).resolve()
    if not root.is_dir():
        raise ValueError(f'Project directory does not exist: {root}')
    findings = []

    def report(path, line, code, message):
        findings.append(f'{path.relative_to(root).as_posix()}:{line}: {code}: {message}')

    for path in markdown_files(root):
        content = path.read_text(encoding='utf-8-sig')
        lines = list(visible_lines(content))
        definitions = {}
        for number, line in enumerate(lines, 1):
            match = re.match(r'^\s{0,3}\[([^]]+)\]:\s*(<[^>]+>|\S+)', line)
            if match:
                definitions[' '.join(match[1].lower().split())] = match[2].strip('<>')

        def check_link(raw, number):
            try:
                url = urlsplit(raw)
            except ValueError:
                report(path, number, 'invalid-link', raw)
                return
            if url.scheme or url.netloc:
                return
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_relative_to(root):
                report(path, number, 'outside-root', raw)
                return
            if not target.exists():
                report(path, number, 'broken-link', raw)
            elif url.fragment and target.is_file() and target.suffix.lower() == '.md':
                if unquote(url.fragment) not in anchors(target.read_text(encoding='utf-8-sig')):
                    report(path, number, 'broken-anchor', raw)

        for number, line in enumerate(lines, 1):
            definition = re.match(r'^\s{0,3}\[([^]]+)\]:\s*(<[^>]+>|\S+)', line)
            if definition:
                check_link(definition[2].strip('<>'), number)
                continue
            for match in re.finditer(r'!?\[[^]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\s*\)', line):
                check_link(match[1].strip('<>'), number)
            for match in re.finditer(r'!?\[([^]\n]+)\]\[([^]\n]*)\]', line):
                key = ' '.join((match[2] or match[1]).lower().split())
                if key not in definitions:
                    report(path, number, 'undefined-reference', key)

    for kind, directory in [('RFC', rfc_dir), ('ADR', adr_dir)]:
        folder = (root / directory).resolve()
        if not folder.is_relative_to(root):
            raise ValueError(f'{kind} directory must be inside the project')
        if not folder.exists():
            continue
        seen = {}
        for path in sorted(folder.glob('*.md')):
            if path.is_symlink() or path.name.lower() in {'readme.md', 'index.md'}:
                continue
            match = re.fullmatch(r'(\d{4})-[\w-]+\.md', path.name)
            if not match:
                report(path, 1, 'invalid-numbering', 'Expected NNNN-title.md')
            elif match[1] in seen:
                report(path, 1, 'duplicate-number', f'{match[1]} also used by {seen[match[1]]}')
            else:
                seen[match[1]] = path.name
            content = '\n'.join(visible_lines(path.read_text(encoding='utf-8-sig')))
            statuses = re.findall(r'^Status:\s*([^\n]+)', content, re.M)
            if len(statuses) != 1 or statuses[0].strip() not in STATES[kind]:
                report(path, 1, 'invalid-status', f'{kind}: expected exactly one supported Status field')
            if kind == 'RFC' and not re.search(r'^Implementação:[ \t]*\S[^\n]*$', content, re.M):
                report(path, 1, 'missing-implementation', 'RFC needs separate Implementação field')
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', type=Path)
    parser.add_argument('--rfc-dir', default='docs/rfcs')
    parser.add_argument('--adr-dir', default='docs/adrs')
    args = parser.parse_args()
    try:
        findings = audit(args.root, args.rfc_dir, args.adr_dir)
    except (OSError, UnicodeError, ValueError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 2
    print('\n'.join(findings) if findings else 'No mechanical findings.')
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main())
