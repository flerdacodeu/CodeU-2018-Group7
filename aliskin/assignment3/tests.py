import unittest
from dictionary import Dictionary
from search import word_search

class TestWordSearchSimple(unittest.TestCase):
    def setUp(self):
        words = ['car', 'cat', 'card', 'cart']
        self.dictionary = Dictionary(words)
        self.grid = [['a', 'a', 'r'], ['t', 'c', 'd']]

    def test_example(self):
        self.assertEqual(word_search(self.grid, self.dictionary), set(['car',
            'cat', 'card']))

    def test_empty_dict(self):
        self.assertEqual(word_search(self.grid, Dictionary([])), set())

    def test_empty_grid(self):
        self.assertEqual(word_search([], self.dictionary), set())

class TestWordSearch(unittest.TestCase):
    def setUp(self):
        words = ['a' * x for x in range(1, 11)]
        self.dictionary = Dictionary(words)
        self.grid = [list('a' * 4) for i in range(4)]

    def test_bla(self):
        self.assertEqual(word_search(self.grid, self.dictionary),
                set(self.dictionary.words))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestWordSearchSimple('test_example'))
    suite.addTest(TestWordSearchSimple('test_empty_dict'))
    suite.addTest(TestWordSearchSimple('test_empty_grid'))
    suite.addTest(TestWordSearch('test_bla'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__ == '__main__':
    main()

