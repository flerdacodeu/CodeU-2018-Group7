import unittest
import string
from alphabet import compute_alphabet

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

def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestExample('test_example'))
    suite.addTest(TestInconsistentDict('test_inconsistent'))
    suite.addTest(TestAlphabet('test_alphabet'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(create_suite())

if __name__ == '__main__':
    main()
