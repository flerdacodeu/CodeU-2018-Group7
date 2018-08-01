import unittest
import random
from assignment6 import compute_moves, compute_efficient_moves, apply_moves


class TestExample(unittest.TestCase):
    def setUp(self):
        self.start_state = [1, 2, 0, 3]
        self.end_state = [3, 1, 2, 0]
        
    def test_compute_moves(self):
        # test the simple function
        moves = compute_moves(self.start_state, self.end_state)
        self.assertEqual(apply_moves(self.start_state, moves), self.end_state)

    def test_compute_efficient_moves(self):
        # test the efficient function, challenge #2
        moves = compute_efficient_moves(self.start_state, self.end_state)
        self.assertEqual(apply_moves(self.start_state, moves), self.end_state)
    
    def test_moves(self):
        moves = compute_efficient_moves(self.start_state, self.end_state)
        self.assertEqual(list(moves), [(1, 2), (0, 1), (3, 0)])

class TestInput(unittest.TestCase):
    # These test cases can be applied either to compute_moves() 
    # or to compute_efficient_moves()
    
    def test_two_empty_states(self):
        # test if both states are empty
        start_state = []
        end_state = []
        moves = compute_efficient_moves(start_state, end_state)
        self.assertRaises(IndexError, lambda: next(moves))
    
    def test_empty_state(self):
        # test if one of the states is empty
        start_state = [1, 2, 0, 3]
        end_state = []
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


class TestEfficientFunction(unittest.TestCase):
    def test_two_cycles(self):
        start_state = [1, 2, 0, 3, 4, 5]
        end_state = [3, 1, 2, 0, 5, 4]
        moves = list(compute_efficient_moves(start_state, end_state))
        self.assertEqual(apply_moves(start_state, moves), end_state)
        self.assertEqual(len(moves), 6)

    def test_random_permutation(self):
        random.seed(31)
        start_state = list(range(100000))
        random.shuffle(start_state)
        end_state = list(range(100000))
        random.shuffle(end_state)
        moves = compute_efficient_moves(start_state, end_state)
        self.assertEqual(apply_moves(start_state, moves), end_state)

    def test_pair_permutations(self):
        start_state = [2, 1, 4, 3, 6, 5, 7, 0]
        end_state = [1, 2, 3, 4, 5, 6, 7, 0]
        moves = list(compute_efficient_moves(start_state, end_state))
        self.assertEqual(apply_moves(start_state, moves), end_state)
        self.assertEqual(len(list(moves)), 9)


if __name__ == '__main__':
    unittest.main()
    