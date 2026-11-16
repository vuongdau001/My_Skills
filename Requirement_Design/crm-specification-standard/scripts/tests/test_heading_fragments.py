"""Unicode heading links, duplicate slug allocation and source boundaries."""
from pathlib import Path
import importlib.util
import unicodedata
from urllib.parse import quote
import unittest

PACK = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('heading_validator', PACK / 'scripts/validate_reference_pack.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class HeadingFragmentTests(unittest.TestCase):
    def test_vietnamese_diacritics_survive_nfc_nfd_and_uri_encoding(self):
        title = 'B02 Dữ liệu thiếu hoặc sai format'
        expected = 'b02-dữ-liệu-thiếu-hoặc-sai-format'
        for value in (title, unicodedata.normalize('NFD', title)):
            self.assertEqual(v.heading_slug(value), expected)
        self.assertEqual(v.normalize_fragment(quote(expected)), expected)
        self.assertEqual(v.normalize_fragment(unicodedata.normalize('NFD', expected)), expected)

    def test_duplicate_suffixes_cannot_collide_with_literal_numbered_titles(self):
        text = '# A\n# A-1\n# A\n# A-1\n'
        slugs = [slug for slug, _, _ in v.heading_anchors(text)]
        self.assertEqual(slugs, ['a', 'a-1', 'a-2', 'a-1-1'])
        self.assertEqual(len(slugs), len(set(slugs)))

    def test_visible_headings_support_markup_and_ignore_fences_comments(self):
        text = '## B02 **Dữ liệu** và `Tax`\n\n```md\n## Giả định\n```\n<!--\n## Ẩn\n-->\n'
        anchors, explicit = v.anchors(text)
        self.assertEqual(anchors, {'b02-dữ-liệu-và-tax'})
        self.assertEqual(explicit, [])
