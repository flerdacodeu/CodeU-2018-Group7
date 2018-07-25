import unittest
from assignment6 import compute_moves, compute_efficient_moves, apply_moves


class Test(unittest.TestCase):
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
    
    # The next two test cases can be applied either to compute_moves() 
    # or to compute_efficient_moves()
    def test_two_empty_states(self):
        # test if both states are empty
        start_state = []
        end_state = []
        moves = compute_efficient_moves(start_state, end_state)
        self.assertRaises(StopIteration, lambda: next(moves))
    
    def test_empty_state(self):
        # test if one of the states is empty
        end_state = []
        moves = compute_efficient_moves(self.start_state, end_state)
        self.assertRaises(IndexError, lambda: next(moves))
    
    def test_apply_to_empty(self):
        # test applying the moves to the empty start state
        start_state = []
        moves = compute_moves(self.start_state, self.end_state)
        self.assertRaises(IndexError, lambda: apply_moves(start_state, moves))
    
    def test_apply_empty_moves(self):
        # test applying an empty sequence of moves to the start state
        moves = []
        self.assertEqual(apply_moves(self.start_state, moves), self.start_state)


if __name__ == '__main__':
    unittest.main()
