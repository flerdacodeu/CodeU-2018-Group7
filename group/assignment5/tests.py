import unittest
import string
from assignment5.find_alphabet import find_alphabet
from assignment5.find_all_alphabets import find_all_alphabets

class Test(unittest.TestCase):
    def test_example(self):
        input_dict = ['ART', 'RAT', 'CAT', 'CAR']
        self.assertIn(find_alphabet(input_dict),[['A', 'T', 'R', 'C'],
                                                 ['T', 'A', 'R', 'C']])

    def test_empty_dict(self):
        input_dict = []
        self.assertEqual(find_alphabet(input_dict), [])

    def test_one_word(self):
        input_dict = ['a']
        self.assertEqual(find_alphabet(input_dict), ['a'])

    def test_inconsistent_dict_none(self):
        input_dict = ['ab', 'bb', 'ba']
        self.assertIsNone(find_alphabet(input_dict), None)

    def test_inconsistent_dict_return_constraints(self):
        input_dict = ['ab', 'bb', 'ba']
        self.assertIn(find_alphabet(input_dict, return_constraints=True),
                      [{'ab'}, {'bb'}, {'ba'}])

    def test_alphabet(self):
        input_dict = [s for s in string.ascii_uppercase]
        self.assertEqual(input_dict, find_alphabet(input_dict))

    def test_alphabet_return_constraints(self):
        input_dict = [s for s in string.ascii_uppercase]
        self.assertSetEqual(
            find_alphabet(input_dict, return_constraints=True), set())

    def test_example_all(self):
        input_dict = ['ART', 'RAT', 'CAT', 'CAR']
        self.assertEqual(find_all_alphabets(input_dict), {'ATRC', 'TARC'})

    def test_one_word(self):
        input_dict = ['ABCDEF']
        self.assertEqual(len(find_all_alphabets(input_dict)), 720)

    def test_two_components(self):
        input_dict = ['AB', 'BC', 'BD']
        self.assertEqual(find_all_alphabets(input_dict), {'ABCD', 'ACBD', 'ACDB', 'CDAB',
            'CADB', 'CABD'})

    def test_all_alphabets(self):
        input_dict = [s for s in string.ascii_uppercase]
        self.assertEqual(find_all_alphabets(input_dict), {string.ascii_uppercase})

if __name__ == '__main__':
    unittest.main()
