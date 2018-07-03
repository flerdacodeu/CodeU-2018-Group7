import unittest
from map_class import Map
from count_islands import count_islands

class TestEmptyMap(unittest.TestCase):
    def setUp(self):
        self.map_ = Map([[False for i in range(100)] for j in range(100)])

    def test_empty_map(self):
        self.assertEqual(count_islands(self.map_), 0)

class TestFullMap(unittest.TestCase):
    def setUp(self):
        self.map_ = Map([[True for i in range(100)] for j in range(10)])

    def test_full_map(self):
        self.assertEqual(count_islands(self.map_), 1)

class TestChessMap(unittest.TestCase):
    def setUp(self):
        size = 100
        map_items = [[False for i in range(size)] for j in range(size)]
        for i in range(size):
            for j in range(size):
                if (i + j) % 2 == 0:
                    map_items[i][j] = True
        self.map_ = Map(map_items)

    def test_chess_map(self):
        self.assertEqual(count_islands(self.map_), self.map_.x_max * self.map_.y_max // 2)

class TestInnerSea(unittest.TestCase):
    def setUp(self):
        self.map_ = Map([[True, True, True, True],
                         [True, False, False, True],
                         [True, True, True, True]])

    def test_inner_sea(self):
        self.assertEqual(count_islands(self.map_), 1)

class TestInnerIsland(unittest.TestCase):
    def setUp(self):
        self.map_ = Map([[True, True, True, True, True],
                         [True, False, False, False, True],
                         [True, False, True, False, True],
                         [True, False, False, False, True],
                         [True, True, True, True, True]])

    def test_inner_island(self):
        self.assertEqual(count_islands(self.map_), 2)

class TestExample(unittest.TestCase):
    def setUp(self):
        self.map_ = Map([[False, True, False, True],
                         [True, True, False, False],
                         [False, False, True, False],
                         [False, False, True, False]])

    def test_example_map(self):
        self.assertEqual(count_islands(self.map_), 3)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestEmptyMap("test_empty_map"))
    suite.addTest(TestFullMap("test_full_map"))
    suite.addTest(TestExample("test_example_map"))
    suite.addTest(TestChessMap("test_chess_map"))
    suite.addTest(TestInnerSea("test_inner_sea"))
    suite.addTest(TestInnerIsland("test_inner_island"))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__ == '__main__':
    main()

