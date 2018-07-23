import unittest
import string
from assignment5.find_alphabet import find_alphabet, find_constraints, find_dictionary
from assignment5.find_all_alphabets import find_all_alphabets


class Test(unittest.TestCase):
    def test_example(self):
        # test finding an alphabet for a simple example
        input_dict = ['ART', 'RAT', 'CAT', 'CAR']
        self.assertIn(find_alphabet(input_dict), {'ATRC', 'TARC'})

    def test_empty_dict(self):
        # finding an alphabet for an empty dictionary
        input_dict = []
        self.assertEqual(find_alphabet(input_dict), [])

    def test_one_word(self):
        # finding an alphabet based on one character
        input_dict = ['a']
        self.assertEqual(find_alphabet(input_dict), ['a'])

    def test_inconsistent_dict_constraints(self):
        # finding constraints for an inconsistent dictionary (challenge 2)
        input_dict = ['ab', 'bb', 'ba']
        self.assertIn(find_constraints(input_dict),
                      [{'ab'}, {'bb'}, {'ba'}])

    def test_inconsistent_maximal_consistent_dict(self):
        # finding a possible maximal consistent dictionary (challenge 3)
        input_dict = ['ab', 'bb', 'ba']
        self.assertIn(find_dictionary(input_dict),
                      [['ab', 'bb'], ['bb', 'ba'], ['ab', 'ba']])

    def test_alphabet(self):
        # finding an alphabet for all ascii letters
        input_dict = [s for s in string.ascii_uppercase]
        self.assertEqual(string.ascii_uppercase, find_alphabet(input_dict))

    def test_alphabet_constraints(self):
        # finding constraints for a consistent dictionary (challenge 2)
        input_dict = [s for s in string.ascii_uppercase]
        self.assertSetEqual(
            find_constraints(input_dict), set())

    def test_alphabet_maximal_consistent_dict(self):
        # finding a maximal consistent dictionary for all ascii letters
        input_dict = [s for s in string.ascii_uppercase]
        self.assertEqual(
            find_dictionary(input_dict), input_dict)

    def test_example_all(self):
        # output all possible alphabets (challenge 1)
        input_dict = ['ART', 'RAT', 'CAT', 'CAR']
        self.assertEqual(find_all_alphabets(input_dict), {'ATRC', 'TARC'})

    def test_one_word(self):
        # output all possible alphabets for one word (challenge 1)
        input_dict = ['ABCDEF']
        self.assertEqual(len(find_all_alphabets(input_dict)), 720)

    def test_two_components(self):
        #  output all possible alphabets (challenge 1)
        input_dict = ['AB', 'BC', 'BD']
        self.assertEqual(find_all_alphabets(input_dict), {'ABCD', 'ACBD', 'ACDB', 'CDAB',
                                                          'CADB', 'CABD'})

    def test_all_alphabets(self):
        # output all possible alphabets for ascii letters
        input_dict = [s for s in string.ascii_uppercase]
        self.assertEqual(find_all_alphabets(input_dict), {string.ascii_uppercase})

if __name__ == '__main__':
    unittest.main()
