import unittest
from assignment5.find_alphabet import find_alphabet


class Test(unittest.TestCase):
    def test_example(self):
        input_dict = ['ART', 'RAT', 'CAT', 'CAR']
        self.assertIn(find_alphabet(input_dict),[['A', 'T', 'R', 'C'],
                                                 ['T', 'A', 'R', 'C']])

    def test_empty_dict(self):
        input_dict = []
        self.assertEqual(find_alphabet(input_dict), [])

    def test_inconsistent_dict(self):
        input_dict = ['ab', 'bb', 'ba']
        self.assertEqual(find_alphabet(input_dict), None)

if __name__ == '__main__':
    unittest.main()
