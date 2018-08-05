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
from helpers import apply_moves, compute_move, input_check

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
    if len(start_state) != len(end_state):
        raise IndexError('The start state and end state have different lengths.')
    input_check(start_state, end_state)
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
    :yields: move steps. Each move is represented as a tuple with two indeces,
             the 1st index is the number of lot from which we move the car,
             the 2nd index is the number of lot to which we move the car
    """
    if len(start_state) != len(end_state):
        raise IndexError('The start state and end state have different lengths.')
    input_check(start_state, end_state)
