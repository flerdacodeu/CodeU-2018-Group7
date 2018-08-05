import unittest
import random
from assignment6 import compute_moves, compute_efficient_moves, compute_all_moves
from helpers import apply_moves
from path_finder import PathFinder


class TestExample(unittest.TestCase):
    def setUp(self):
        self.start_state = [1, 2, 0, 3]
        self.end_state = [3, 1, 2, 0]

    def test_compute_moves(self):
        # test the simple function
        moves = compute_moves(self.start_state, self.end_state)
        self.assertEqual(apply_moves(self.start_state, moves),
                         self.end_state)

    def test_compute_efficient_moves(self):
        # test the efficient function, challenge #2
        moves = compute_efficient_moves(self.start_state,
                                        self.end_state)
        self.assertEqual(apply_moves(self.start_state, moves),
                         self.end_state)

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
        self.assertEqual(list(moves), list())

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
        self.assertRaises(IndexError,
                          lambda: apply_moves(start_state, moves))

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
        self.assertRaises(IndexError,
                          lambda: apply_moves(start_state, moves))

    def test_same_car_index(self):
        # test having same car on multiple parking lots
        start_state = [2, 2, 2, 0]
        end_state = [2, 2, 2, 0]
        moves = compute_efficient_moves(start_state, end_state)
        self.assertRaises(IndexError,
                          lambda: apply_moves(start_state, moves))

    def test_no_empty_lot(self):
        # test parking without empty parking lots
        start_state = [1, 2, 3]
        end_state = [3, 2, 1]
        moves = compute_efficient_moves(start_state, end_state)
        self.assertRaises(IndexError,
                          lambda: apply_moves(start_state, moves))

    def test_states_not_in_constraints(self):
        # test input states don't satisfy given constraints
        start_state = [0, 1, 2, 3]
        end_state = [0, 2, 1, 3]
        constraints = {0: (1, 3), 1: (0, 1, 2, 3),
                       2: (0, 1, 2, 3), 3: (0, 1, 2, 3)}
        self.assertRaises(ValueError, lambda: PathFinder(start_state,
                                                         end_state,
                                                         constraints))


class TestEfficientFunction(unittest.TestCase):
    def test_two_cycles(self):
        start_state = [1, 2, 0, 3, 4, 5]
        end_state = [3, 1, 2, 0, 5, 4]
        moves = list(compute_efficient_moves(start_state, end_state))
        self.assertEqual(apply_moves(start_state, moves), end_state)
        self.assertEqual(len(moves), 6)

    def test_random_permutation(self):
        random.seed(31)
        parking_size = 100000
        start_state = list(range(parking_size))
        random.shuffle(start_state)
        end_state = list(range(parking_size))
        random.shuffle(end_state)
        moves = compute_efficient_moves(start_state, end_state)
        self.assertEqual(apply_moves(start_state, moves), end_state)

    def test_pair_permutations(self):
        start_state = [2, 1, 4, 3, 6, 5, 7, 0]
        end_state = [1, 2, 3, 4, 5, 6, 7, 0]
        moves = list(compute_efficient_moves(start_state, end_state))
        self.assertEqual(apply_moves(start_state, moves), end_state)
        self.assertEqual(len(list(moves)), 9)

    def test_efficient(self):
        # compute efficient moves and then
        # check if it is really the shortest one
        start_state = [0, 1, 2, 3]
        end_state = [0, 2, 1, 3]
        moves = list(compute_efficient_moves(start_state, end_state))
        all_sequences = list(compute_all_moves(start_state, end_state))
        min_length = min(len(sequence) for sequence in all_sequences)
        shortest_sequences = [sequence for sequence in all_sequences
                              if len(sequence) == min_length]
        self.assertIn(moves, shortest_sequences)


class TestAllMoves(unittest.TestCase):
    def test_all_moves_empty_states(self):
        start_state = []
        end_state = []
        moves = list(compute_all_moves(start_state, end_state))
        self.assertEqual(moves, [])

    def test_all_moves_simple_case(self):
        start_state = [0, 1]
        end_state = [1, 0]
        moves = list(compute_all_moves(start_state, end_state))
        self.assertEqual(moves, [[(1, 0)]])

if __name__ == '__main__':
    unittest.main()
