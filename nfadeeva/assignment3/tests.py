from assignment3.dictionary import Dictionary
from assignment3.search_words import search_words, Grid
import unittest


class Test(unittest.TestCase):

    def setUp(self):
        self.d = Dictionary(['CAR', 'CAT', 'CARD', 'CART'])

    # tests for the Dictionary class
    def test_is_word_true(self):
        self.assertTrue(self.d.is_word('CAR'))

    def test_is_word_false(self):
        self.assertFalse(self.d.is_word('CA'))

    def test_is_prefix_true(self):
        self.assertTrue(self.d.is_prefix('CA'))

    def test_is_prefix_false(self):
        self.assertFalse(self.d.is_prefix('D'))

    # tests for the whole solution
    def test_example(self):
        g = Grid([['A', 'A', 'R'], ['T', 'C', 'D']])
        self.assertSetEqual(search_words(g, self.d), {'CAT', 'CAR', 'CARD'})

    def test_empty_dict(self):
        g = Grid([['A', 'A', 'R']])
        d = Dictionary([])
        self.assertEqual(search_words(g, d), set())

    def test_empty_grid(self):
        g = Grid([[]])
        self.assertEqual(search_words(g, self.d), set())


if __name__ == '__main__':
    unittest.main()
