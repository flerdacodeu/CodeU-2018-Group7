import unittest
from assignment5 import compute_alphabet, AlphabetError
from assignment5_graph import Graph


class Test(unittest.TestCase):

    def setUp(self):
        self.dictionary = ['ART', 'RAT', 'CAT', 'CAR']
        self.g = Graph(self.dictionary)
        
    
    # Tests for the simple function with rules

    # tests the simple function
    def test_compute_alphabet(self):
        alphabet = compute_alphabet(self.dictionary)
        self.assertEqual(alphabet, ['A', 'T', 'R', 'C'])

    # test if the dictionary is empty
    def test_empty_dic(self):
        dictionary = []
        g = Graph(dictionary)
        alphabet1 = compute_alphabet(dictionary)
        alphabet2 = g.topological_sort()
        self.assertEqual(alphabet1, [])
        self.assertEqual(alphabet2, [])
        
    # test a dictionary with an error, not yet implemented for topological sort!
    def test_inconsistent_dic(self):
        dictionary = ['ART', 'RAT', 'CAT', 'CAR', 'RAC']
        self.assertRaises(AlphabetError, lambda: compute_alphabet(dictionary))
    
    # Tests for the graph solution
    def test_topological_sort(self):
        alphabet = self.g.topological_sort()
        self.assertTrue(alphabet in [['A', 'T', 'R', 'C'], ['T', 'A', 'R', 'C']]);


if __name__ == '__main__':
    unittest.main()
