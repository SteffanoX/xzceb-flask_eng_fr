import unittest
from final_project.machinetranslation.translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french('hello'), '')

    def test2(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')



class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english('Bonjour'), '')


    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()

