import unittest
import random
from rearrange_cars import rearrange_cars_naive, rearrange_cars

def apply_moves_sequence(start_state, moves_sequence):
    current_state = start_state.copy()
    for car, lot_from, lot_to in moves_sequence:
        if current_state[lot_to] != 0:
            raise ValueError("Parking lot {} should be empty but it's not.".format(lot_to))
        current_state[lot_to] = car
        current_state[lot_from] = 0
    return current_state

class TestExample(unittest.TestCase):
    def setUp(self):
        self.start_state = [1, 2, 0, 3]
        self.end_state = [3, 1, 2, 0]

    def test_example_naive(self):
        moves_sequence = rearrange_cars_naive(self.start_state, self.end_state)
        self.assertEqual(apply_moves_sequence(self.start_state, moves_sequence), self.end_state)

    def test_example(self):
        moves_sequence = rearrange_cars(self.start_state, self.end_state)
        self.assertEqual(moves_sequence, [(2, 1, 2), (1, 0, 1), (3, 3, 0)])

class TestOptimalSequence(unittest.TestCase):
    def test_two_cycles(self):
        start_state = [1, 2, 0, 3, 4, 5]
        end_state = [3, 1, 2, 0, 5, 4]
        moves_sequence = rearrange_cars(start_state, end_state)
        self.assertEqual(apply_moves_sequence(start_state, moves_sequence), end_state)
        self.assertEqual(len(moves_sequence), 6)

    def test_random_permutation(self):
        random.seed(31)
        start_state = list(range(100))
        random.shuffle(start_state)
        end_state = list(range(100))
        random.shuffle(end_state)
        moves_sequence = rearrange_cars(start_state, end_state)
        self.assertEqual(apply_moves_sequence(start_state, moves_sequence), end_state)

    def test_pair_permutations(self):
        start_state = [2, 1, 4, 3, 6, 5, 7, 0]
        end_state = [1, 2, 3, 4, 5, 6, 7, 0]
        moves_sequence = rearrange_cars(start_state, end_state)
        self.assertEqual(apply_moves_sequence(start_state, moves_sequence), end_state)
        self.assertEqual(len(moves_sequence), 9)


def create_suite():
    suite = unittest.TestSuite()
    suite.addTest(TestExample("test_example_naive"))
    suite.addTest(TestExample("test_example"))
    suite.addTest(TestOptimalSequence("test_two_cycles"))
    suite.addTest(TestOptimalSequence("test_random_permutation"))
    suite.addTest(TestOptimalSequence("test_pair_permutations"))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(create_suite())

if __name__ == '__main__':
    main()
