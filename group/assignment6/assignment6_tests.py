import unittest
import random
from path_finder import PathFinder


class TestExample(unittest.TestCase):
    def setUp(self):
        self.start_state = [1, 2, 0, 3]
        self.end_state = [3, 1, 2, 0]
        self.path_finder = PathFinder(self.start_state, self.end_state)
        
    def test_compute_moves(self):
        # test the simple function
        moves = self.path_finder.compute_moves()
        self.assertEqual(self.path_finder.apply_moves(moves), self.end_state)

    def test_compute_efficient_moves(self):
        # test the efficient function, challenge #2
        moves = self.path_finder.compute_efficient_moves()
        self.assertEqual(self.path_finder.apply_moves(moves), self.end_state)
    
    def test_moves(self):
        moves = self.path_finder.compute_efficient_moves()
        self.assertEqual(list(moves), [(1, 2), (0, 1), (3, 0)])


class TestInput(unittest.TestCase):
    # These test cases can be applied either to compute_moves()
    # or to compute_efficient_moves()

    def test_two_empty_states(self):
        # test if both states are empty
        start_state = []
        end_state = []
        path_finder = PathFinder(start_state, end_state)
        moves = path_finder.compute_efficient_moves()
        self.assertEqual(list(moves), list())

    def test_empty_state(self):
        # test if one of the states is empty
        start_state = [1, 2, 0, 3]
        end_state = []
        path_finder = PathFinder(start_state, end_state)
        moves = compute_efficient_moves(start_state, end_state)
        self.assertRaises(IndexError, lambda: next(moves))

    def test_apply_to_empty(self):
        # test applying the moves to the empty start state
        start_state = []
        moves = [(1, 2), (0, 1), (3, 0)]
        self.assertRaises(IndexError, lambda: apply_moves(start_state, moves))

    def test_apply_empty_moves(self):
        # test applying an empty sequence of moves to the start state
        moves = []
        start_state = [1, 2, 0, 3]
        self.assertEqual(apply_moves(start_state, moves), start_state)

    def test_nonexistent_indexes(self):
        # test trying to move cars with nonexistent indexes
        start_state = [1, 2, 0, 3]
        end_state = [123, 0, 143, 79]
        moves = compute_efficient_moves(start_state, end_state)
        self.assertRaises(IndexError, lambda: apply_moves(start_state, moves))

    def test_same_car_index(self):
        # test having same car on multiple parking lots
        start_state = [2, 2, 2, 0]
        end_state = [2, 2, 2, 0]
        moves = compute_efficient_moves(start_state, end_state)
        self.assertRaises(IndexError, lambda: apply_moves(start_state, moves))

    def test_no_empty_lot(self):
        # test parking without empty parking lots
        start_state = [1, 2, 3]
        end_state = [3, 2, 1]
        moves = compute_efficient_moves(start_state, end_state)
        self.assertRaises(IndexError, lambda: apply_moves(start_state, moves))


class TestEfficientFunction(unittest.TestCase):
    def test_two_cycles(self):
        start_state = [1, 2, 0, 3, 4, 5]
        end_state = [3, 1, 2, 0, 5, 4]
        path_finder = PathFinder(start_state, end_state)
        moves = list(path_finder.compute_efficient_moves())
        self.assertEqual(path_finder.apply_moves(moves), end_state)
        self.assertEqual(len(moves), 6)

    def test_random_permutation(self):
        random.seed(31)
        parking_size = 100000
        start_state = list(range(parking_size))
        random.shuffle(start_state)
        end_state = list(range(parking_size))
        random.shuffle(end_state)
        path_finder = PathFinder(start_state, end_state)
        moves = path_finder.compute_efficient_moves()
        self.assertEqual(path_finder.apply_moves(moves), end_state)

    def test_pair_permutations(self):
        start_state = [2, 1, 4, 3, 6, 5, 7, 0]
        end_state = [1, 2, 3, 4, 5, 6, 7, 0]
        path_finder = PathFinder(start_state, end_state)
        moves = list(path_finder.compute_efficient_moves())
        self.assertEqual(path_finder.apply_moves(moves), end_state)
        self.assertEqual(len(list(moves)), 9)

if __name__ == '__main__':
    unittest.main()
