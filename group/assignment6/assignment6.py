"""
There is a parking lot with N spaces and N-1 cars in it. Below is
an algorithm to rearrange the cars in a given way. Only one car can be
moved at a time to the empty slot. Start state and end state are
represented as lists of car numbers, and 0 signifies empty slot.
Thus, a number of a lot in which a car is placed is an index of that car
number in the list. For example, [1, 2, 0, 3] is the start state.
Car #1 is in the lot #0, car #2 is in the lot #1, etc.
"""

from parking_class import Parking
from path_finder import PathFinder
from helpers import compute_move, check_input_validity


def compute_moves(start_state, end_state):
    """
    Computes a sequence of moves that are required to rearrange cars
    from the given start state to the end state.
    For every lot number we look up which car should be placed in this lot.
    The current car is moved to the empty lot, the correct car is moved
    to the current lot.
    :param start_state: order of cars in the start of the rearrangement
    :param end_state: order of cars after rearrangement
    :yields: move steps. Each move is represented as a tuple with two indeces,
             the first index is the number of lot from which we move the car,
             the second index is the number of lot to which we move the car
    """
    check_input_validity(start_state, end_state)
    parking = Parking(start_state.copy())
    for lot in range(len(parking)):
        end_car = end_state[lot]
        if parking.get_car(lot) == end_car or end_car == 0:
            continue
        if parking.get_car(lot) != 0:
            yield parking.move_to_empty_lot(parking.get_car(lot))
        yield parking.move_to_empty_lot(end_car)


def compute_efficient_moves(start_state, end_state):
    """
    More efficiently computes the shortest sequence of moves that are required to rearrange
    cars from the given start state to the end state. We look up which lot is
    empty and which car should be in this lot. Then we move the required car
    to the empty lot and repeat the procedure.
    If empty slot is empty in the end state too, we take the leftmost lot
    with the misplaced car and move the car from that lot to the empty one.
    Then we perform the initial steps. When all the cars are on their places
    (misplaced_car == len(current_state)), algorithm is finished.
    :param start_state: order of cars in the start of the rearrangement
    :param end_state: order of cars after rearrangement
    :yields: move steps. Each move is represented as a tuple with two indices,
             the 1st index is the number of lot from which we move the car,
             the 2nd index is the number of lot to which we move the car
    """
    check_input_validity(start_state, end_state)
    parking = Parking(start_state.copy())
    misplaced_car_lot = 0
    while misplaced_car_lot < len(parking):
        empty_lot = parking.find_empty_lot()
        while end_state[empty_lot] != 0:
            end_car = end_state[empty_lot]
            yield parking.move_to_empty_lot(end_car)
            empty_lot = parking.find_empty_lot()
        while (misplaced_car_lot < len(parking) and end_state[misplaced_car_lot] ==
               parking.get_car(misplaced_car_lot)):
            misplaced_car_lot += 1
        if misplaced_car_lot < len(parking):
            yield parking.move_to_empty_lot(parking.get_car(misplaced_car_lot))


def compute_moves_with_constraints(start_state, end_state, constraints):
    """
    Computes moves sequence under given constraints.
    :param start_state: order of cars in the start of the rearrangement
    :param end_state: order of cars after rearrangement
    :param constraints: map from the parking lot to a tuple of the allowed cars
    :yields: move steps. Each move is represented as a tuple with two indices,
             the 1st index is the number of lot from which we move the car,
             the 2nd index is the number of lot to which we move the car
    """
    check_input_validity(start_state, end_state)
    path_finder = PathFinder(tuple(start_state), tuple(end_state), constraints)
    paths = path_finder.find_all_paths()
    path = path_finder.decode_path(next(paths))
    for i in range(1, len(path)):
        yield compute_move(path[i - 1], path[i])


def compute_all_moves(start_state, end_state):
    """
    Computes all possible ways to rearrange the cars from
    start_state to end_state.
 
    :param start_state: order of cars in the start of the rearrangement
    :param end_state: order of cars after rearrangement
    :yields: a list of move steps. Each move is represented as a tuple
             with two indeces,
             the 1st index is the number of lot from which we move the car,
             the 2nd index is the number of lot to which we move the car
    """
    check_input_validity(start_state, end_state)
    parking_size = len(start_state)
    constraints = {i: tuple(range(parking_size))
                   for i in range(parking_size)}
    path_finder = PathFinder(tuple(start_state), tuple(end_state),
                             constraints=constraints)
    paths = path_finder.find_all_paths()
    for path in paths:
        decoded_path = path_finder.decode_path(path)
        moves_sequence = list()
        for i in range(1, len(decoded_path)):
            moves_sequence.append(
                compute_move(decoded_path[i - 1], decoded_path[i]))
        yield moves_sequence
   

def main():
    start_state = [1, 2, 3, 0]
    end_state = [3, 1, 2, 0]

    print("Computing a moves sequence for the main problem...")
    moves = list(compute_moves(start_state, end_state))
    print(moves)

    print("Computing the shortest moves sequence...")
    moves = list(compute_efficient_moves(start_state, end_state))
    print(moves)

    print("Computing a moves sequence under given constraints...")
    constraints = {0: (1, 3), 1: (0, 1, 2, 3),
                   2: (0, 1, 2, 3), 3: (0, 1, 2, 3)}
    moves = list(compute_moves_with_constraints(
        start_state, end_state, constraints))
    print(moves)

    print("Computing all moves sequences between two parking states...")
    moves_sequences = list(compute_all_moves(start_state, end_state))
    n_sequences = len(moves_sequences)
    n = min(5, n_sequences)
    print("Found {} possible moves sequences,"
          " printing first {} moves sequences:".format(n_sequences, n))
    for moves in moves_sequences[:n]:
        print(moves)

if __name__ == '__main__':
    main()
