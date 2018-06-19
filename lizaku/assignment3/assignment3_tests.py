import unittest
from assignment3 import Grid, find_words, Dictionary


class Test(unittest.TestCase):

    def setUp(self):
        self.vocab = Dictionary(['card', 'cart', 'cat', 'car', 'a'])
        self.grid = Grid([['a', 'a', 'r'], ['t', 'c', 'd']])

    # tests for isPrefix and isWord
    def test_is_word(self):
        self.assertTrue(self.vocab.isWord('cat'))
        self.assertFalse(self.vocab.isWord('c'))

    def test_is_prefix(self):
        self.assertTrue(self.vocab.isPrefix('ca'))
        self.assertFalse(self.vocab.isPrefix('at'))
        

    # tests the main function
    def test_find_words(self):
        self.assertSetEqual(find_words(self.grid, self.vocab), {'card', 'car', 'cat', 'a'})

    def test_empty_dict(self):
        vocab = Dictionary([])
        self.assertEqual(find_words(self.grid, vocab), set())

    def test_empty_grid(self):
        grid = Grid([[]])
        self.assertEqual(find_words(grid, self.vocab), set())


if __name__ == '__main__':
    unittest.main()
