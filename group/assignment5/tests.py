import unittest
import string
from alphabet import compute_alphabet, compute_all_alphabets

class TestExample(unittest.TestCase):
    def setUp(self):
        self.dictionary = ['ART', 'RAT', 'CAT', 'CAR']

    def test_example(self):
        self.assertIn(compute_alphabet(self.dictionary), 
                [['A', 'T', 'R', 'C'],
                 ['T', 'A', 'R', 'C']])

class TestInconsistentDict(unittest.TestCase):
    def setUp(self):
        self.dictionary = ['A', 'R', 'A']

    def test_inconsistent(self):
        self.assertRaises(ValueError, compute_alphabet, self.dictionary)

class TestAlphabet(unittest.TestCase):
    def setUp(self):
        self.dictionary = [s for s in string.ascii_uppercase]

    def test_alphabet(self):
        self.assertEqual(compute_alphabet(self.dictionary), self.dictionary)

    def test_all_alphabets(self):
        self.assertEqual(compute_all_alphabets(self.dictionary), {string.ascii_uppercase})

class TestAllAlphabets(unittest.TestCase):
    def test_example(self):
        dictionary = ['ART', 'RAT', 'CAT', 'CAR']
        self.assertEqual(compute_all_alphabets(dictionary),
                {'ATRC', 'TARC'})

    def test_one_word(self):
        dictionary = ['ABCDEF']
        self.assertEqual(len(compute_all_alphabets(dictionary)), 720)

    def test_two_components(self):
        dictionary = ['AB', 'BC', 'BD']
        self.assertEqual(compute_all_alphabets(dictionary), {'ABCD', 'ACBD', 'ACDB', 'CDAB',
            'CADB', 'CABD'})

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestExample('test_example'))
    suite.addTest(TestInconsistentDict('test_inconsistent'))
    suite.addTest(TestAlphabet('test_alphabet'))
    suite.addTest(TestAlphabet('test_all_alphabets'))
    suite.addTest(TestAllAlphabets('test_example'))
    suite.addTest(TestAllAlphabets('test_one_word'))
    suite.addTest(TestAllAlphabets('test_two_components'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(create_suite())

if __name__ == '__main__':
    main()
