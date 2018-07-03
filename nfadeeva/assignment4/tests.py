from assignment4.count_islands import count_islands
import unittest


class Test(unittest.TestCase):
    def test_example(self):
        tiles = [[False, True, False, True],
                       [True, True, False, False],
                       [False, False, True, False],
                       [False, False, True, False]]
        num_rows, num_cols = 4, 4
        self.assertEqual(count_islands(num_rows, num_cols, tiles), 3)

    def test_empty_array(self):
        tiles = []
        num_rows, num_cols = 0, 0
        self.assertEqual(count_islands(num_rows, num_cols, tiles), 0)

    def test_no_islands(self):
        num_rows, num_cols = 4, 3
        tiles = [[False for i in range(num_cols)] for i in range(num_rows)]
        self.assertEqual(count_islands(num_rows, num_cols, tiles), 0)

    def test_one_island(self):
        num_rows, num_cols = 4, 3
        tiles = [[True for i in range(num_cols)] for i in range(num_rows)]
        self.assertEqual(count_islands(num_rows, num_cols, tiles), 1)

if __name__ == '__main__':
    unittest.main()
