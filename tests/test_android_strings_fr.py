"""The French menu texts (StringsFr.java) must stay in step with the English ones they translate."""
import re
import unittest
from pathlib import Path

SETUP = Path(__file__).resolve().parents[1] / 'games/totk/android/java/com/aure/totk/setup'
JAVA_TEXT = r'"((?:[^"\\]|\\.)*)"'
PAIR = re.compile(r'^\s+' + JAVA_TEXT + r',\n\s+' + JAVA_TEXT + r',$', re.M)
PLACEHOLDER = re.compile(r'%[,.\d]*[a-z]')


class FrenchStringsTest(unittest.TestCase):
    def test_every_french_text_translates_an_existing_english_one(self):
        pairs = PAIR.findall((SETUP / 'StringsFr.java').read_text(encoding='utf-8'))
        self.assertGreater(len(pairs), 500)
        sources = ''.join(p.read_text(encoding='utf-8') for p in SETUP.glob('*.java') if p.name != 'StringsFr.java')
        for english, french in pairs:
            with self.subTest(english=english[:60]):
                self.assertIn('"' + english + '"', sources)
                self.assertEqual(sorted(PLACEHOLDER.findall(english)), sorted(PLACEHOLDER.findall(french)))


if __name__ == '__main__':
    unittest.main()
