"""
Find a sequence of moves that rearranges the cars from a given start state to some end state.
A state is represented as a list where each element correponds to a car and zero element
corresponds to an empty lot.
Inverted state is also a list where each element represents a parking lot.
"""

def move_car_to_empty(car, current_state, inverted_current_state, empty_lot):
    """Moves a car from current lot to empty lot and updates current_state and
    inverted_current_state correspondingly.

    Returns:
        new empty lot
    """
    #car = current_state[lot_from]
    lot_from = inverted_current_state[car]
    current_state[empty_lot] = car
    current_state[lot_from] = 0
    inverted_current_state[car] = empty_lot
    inverted_current_state[0] = lot_from
    return lot_from

def place_car_to_lot(car, lot_to, current_state, inverted_state, empty_lot):
    """Moves a given car from its lot to lot_to.

    Returns:
        new empty lot
    """
    #move_car_to_empty(lot_to, current_state, inverted_state, empty_lot)
    empty_lot = move_car_to_empty(current_state[lot_to], current_state, inverted_state, empty_lot)
    lot_from = inverted_state[car]
    return move_car_to_empty(current_state[lot_from], current_state, inverted_state, empty_lot)

def rearrange_cars_naive(start_state, end_state):
    """Given a start state of n parking lots and n - 1 cars computes a sequence of moves that
    rearranges the cars in order to obtain end state.
    Number of moves in the worst case is 2 * n

    Args:
        start_state: a list of ints, each element corresponds to a car, zero corresponds to an
        empty lot
        end_state: same format as start_state

    Returns:
        moves_sequence: one possible sequence of moves
    """
    empty_lot = start_state.index(0)
    current_state = start_state.copy()
    inverted_state = [0 for i in range(len(start_state))]
    moves_sequence = list()
    for lot, car in enumerate(start_state):
        inverted_state[car] = lot
    for lot, car in enumerate(current_state):
        # print(current_state)
        if car == end_state[lot] or end_state[lot] == 0:
            continue
        new_car = end_state[lot]
        # TODO: NamedTuple for move: (Car, From, To)
        moves_sequence.append((car, lot, empty_lot))
        moves_sequence.append((new_car, inverted_state[new_car], lot))
        empty_lot = place_car_to_lot(new_car, lot, current_state, inverted_state, empty_lot)
    # print(current_state)
    # print(moves_sequence)
    return moves_sequence


def rearrange_cars(start_state, end_state):
    """Given a start state of n parking lots and n - 1 cars computes a sequence of moves that
    rearranges the cars in order to obtain end state where number of moves is minimal

    Args:
        start_state: a list of ints, each element corresponds to a car, zero corresponds to an
        empty lot
        end_state: same format as start_state

    Returns:
        moves_sequence: an optimal sequence of moves
    """
    empty_lot = start_state.index(0)
    current_state = start_state.copy()
    inverted_state = [0 for i in range(len(start_state))]
    moves_sequence = list()
    for lot, car in enumerate(start_state):
        inverted_state[car] = lot
    leftest_misplaced_car = 0
    parking_size = len(start_state)

    while leftest_misplaced_car < parking_size:
        while empty_lot != end_state.index(0):
            new_car = end_state[empty_lot]
            moves_sequence.append((new_car, inverted_state[new_car], empty_lot))
            empty_lot = move_car_to_empty(new_car, current_state, inverted_state, empty_lot)

        while (leftest_misplaced_car < parking_size and end_state[leftest_misplaced_car] ==
               current_state[leftest_misplaced_car]):
            leftest_misplaced_car += 1

        if leftest_misplaced_car < parking_size:
            moves_sequence.append((current_state[leftest_misplaced_car], leftest_misplaced_car,
                                   empty_lot))
            empty_lot = move_car_to_empty(current_state[leftest_misplaced_car], current_state,
                                          inverted_state, empty_lot)
    return moves_sequence
