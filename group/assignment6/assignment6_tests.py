import unittest
from assignment6 import compute_moves, compute_efficient_moves, apply_moves


class Test(unittest.TestCase):
    def setUp(self):
        self.start_state = [1, 2, 0, 3]
        self.end_state = [3, 1, 2, 0]
        
    def test_compute_moves(self):
        moves = compute_moves(self.start_state, self.end_state)
        self.assertEqual(apply_moves(self.start_state, moves), self.end_state)

    def test_compute_efficient_moves(self):
        moves = compute_efficient_moves(self.start_state, self.end_state)
        self.assertEqual(apply_moves(self.start_state, moves), self.end_state)


if __name__ == '__main__':
    unittest.main()
