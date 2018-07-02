import unittest
from assignment4 import Grid


class Test(unittest.TestCase):

    def setUp(self):
        self.grid = Grid([[False, True, False, True], 
                          [True, True, False, False],
                          [False, False, True, False],
                          [False, False, True, False]])

    # tests the main function
    def test_find_islands(self):
        islands, num = self.grid.find_islands()
        self.assertEqual(num, 3)

    # test if the Grid is empty
    def test_empty_grid(self):
        grid = Grid([[]])
        islands, num = grid.find_islands()
        self.assertEqual(islands, [])
        self.assertEqual(num, 0)
        
    def test_grid_validity(self):
        grid = [[False, True, False, True, False, True], 
                [True, True, False],
                [False, False, True, False],
                [False],
                []]
        self.assertRaises(IndexError, lambda: Grid(grid))


if __name__ == '__main__':
    unittest.main()
