"""Mechanical checks and preservation evidence; not an automated domain interview."""
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'project-context'
FIXTURE = ROOT / 'validation/fixture'
SPEC = importlib.util.spec_from_file_location('audit_docs', SKILL / 'scripts/audit_docs.py')
AUDITOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(AUDITOR)


class DocumentationChecks(unittest.TestCase):
    def test_skill_and_fixture_local_links(self):
        self.assertEqual(AUDITOR.audit(SKILL), [])
        self.assertEqual(AUDITOR.audit(FIXTURE), [])

    def test_second_pass_preserved_existing_content(self):
        first = ROOT / 'validation/run-1'
        # Later state-routing additions must preserve the original instructions.
        self.assertTrue((FIXTURE / 'AGENTS.md').read_bytes().startswith(
            (first / 'AGENTS.md.txt').read_bytes()))
        self.assertTrue((FIXTURE / 'src/sales/context.md').read_bytes().startswith(
            (first / 'sales-context.md.txt').read_bytes()))
        # These files had no new information in pass 2: preserve exact bytes.
        hashes = json.loads((first / 'hashes.json').read_text(encoding='utf-8-sig'))
        unchanged = ['product.md', 'context-map.md', 'src/sales/service.py',
                     'src/shipping/service.py', 'docs/architecture/current.md']
        for name in unchanged:
            self.assertEqual(hashlib.sha256((FIXTURE / name).read_bytes()).hexdigest(), hashes[name])

    def test_audit_does_not_mutate_files(self):
        before = {p: p.read_bytes() for p in FIXTURE.rglob('*') if p.is_file()}
        AUDITOR.audit(FIXTURE)
        AUDITOR.audit(FIXTURE)
        self.assertEqual(before, {p: p.read_bytes() for p in before})

    def test_links_references_anchors_and_code_blocks(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'target.md').write_text('# Olá mundo\n# Repeat\n# Repeat\n', encoding='utf-8')
            (root / 'page.md').write_text(
                '[ok](target.md#olá-mundo)\n[repeat](target.md#repeat-1)\n'
                '[bad](missing.md)\n[anchor](target.md#missing)\n'
                '[reference][unknown]\n[known][ok]\n[ok]: target.md\n'
                '```md\n[ignored](absent.md)\n```\n'
                '`[ignored](inline.md)`\n[remote](https://example.invalid)\n', encoding='utf-8')
            findings = AUDITOR.audit(root)
            self.assertEqual(len(findings), 3, findings)
            self.assertTrue(any('broken-link' in f and 'missing.md' in f for f in findings))
            self.assertTrue(any('broken-anchor' in f for f in findings))
            self.assertTrue(any('undefined-reference' in f for f in findings))

    def test_independent_sequences_status_and_implementation(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            rfc, adr = root / 'docs/rfcs', root / 'docs/adrs'
            rfc.mkdir(parents=True)
            adr.mkdir(parents=True)
            (rfc / '0001-example.md').write_text('Status: Accepted\nImplementação: Não iniciada\n', encoding='utf-8')
            (adr / '0001-example.md').write_text('Status: Proposed\n', encoding='utf-8')
            self.assertEqual(AUDITOR.audit(root), [])
            (rfc / '0001-duplicate.md').write_text('Status: Finished\n', encoding='utf-8')
            (adr / 'un-numbered.md').write_text('# No status\n', encoding='utf-8')
            findings = AUDITOR.audit(root)
            for code in ['duplicate-number', 'invalid-status', 'missing-implementation', 'invalid-numbering']:
                self.assertTrue(any(code in f for f in findings), findings)

    def test_alternate_directories_and_root_boundary(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'proposals').mkdir()
            (root / 'proposals/0001-example.md').write_text('Status: Draft\n', encoding='utf-8')
            (root / 'index.md').write_text('[outside](../outside.md)\n', encoding='utf-8')
            findings = AUDITOR.audit(root, rfc_dir='proposals')
            self.assertTrue(any('outside-root' in f for f in findings))
            self.assertTrue(any('missing-implementation' in f for f in findings))
            with self.assertRaises(ValueError):
                AUDITOR.audit(root, rfc_dir='../outside')

    def test_cli_exit_codes(self):
        command = [sys.executable, str(SKILL / 'scripts/audit_docs.py')]
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for expected in [0, 1]:
                if expected:
                    (root / 'bad.md').write_text('[missing](missing.md)\n', encoding='utf-8')
                result = subprocess.run(command + [str(root)], capture_output=True)
                self.assertEqual(result.returncode, expected, result.stderr)
            result = subprocess.run(command + [str(root / 'missing')], capture_output=True)
            self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
