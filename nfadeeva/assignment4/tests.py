from assignment4.count_islands import count_islands
import unittest


class Test(unittest.TestCase):
    def test_example(self):
        input_array = [[False, True, False, True],
                       [True, True, False, False],
                       [False, False, True, False],
                       [False, False, True, False]]
        num_rows = 4
        num_cols = 4
        self.assertEqual(count_islands(num_rows, num_cols, input_array), 3)

    def test_empty_array(self):
        input_array = []
        num_rows = 0
        num_cols = 0
        self.assertEqual(count_islands(num_rows, num_cols, input_array), 0)

    def test_no_islands(self):
        num_rows = 4
        num_cols = 3
        input_array = [[False for i in range(num_cols)] for i in range(num_rows)]
        self.assertEqual(count_islands(num_rows, num_cols, input_array), 0)

    def test_one_island(self):
        num_rows = 4
        num_cols = 3
        input_array = [[True for i in range(num_cols)] for i in range(num_rows)]
        self.assertEqual(count_islands(num_rows, num_cols, input_array), 1)

if __name__ == '__main__':
    unittest.main()
