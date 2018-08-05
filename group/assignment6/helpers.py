from parking_class import Parking


def apply_moves(start_state, moves):
    """
    Applies the sequence of moves to a given state.
    :param start_state: order of cars in the start of the rearrangement
    :param moves: generator, sequence of moves that we need to apply.
                  Each move is represented as a tuple with two indices,
                  the 1st index is the number of lot from which we move the car,
                  the 2nd index is the number of lot to which we move the car
    :returns: end state, list of car numbers.
    """
    check_input_validity(start_state)
    parking = Parking(start_state.copy())
    for move in moves:
        move_from, move_to = move
        parking.move_to_empty_lot(parking.get_car(move_from))
    return parking.get_state()


def compute_move(start_state, end_state):
    """
    Computes a move from one state to another under an assumption that end_state differs from
    start_state by one move of some car to an empty lot.
    :returns a tuple
    """
    check_input_validity(start_state, end_state)
    empty_lot = start_state.index(0)
    car = end_state[empty_lot]
    move_from = start_state.index(car)
    return move_from, empty_lot


def check_input_validity(start_state=None, end_state=None):
    if start_state is not None:
        if list(range(len(start_state))) != sorted(start_state):
            raise IndexError('Invalid start state')
        num_of_zeros_start = start_state.count(0)
        if num_of_zeros_start > 1:
            raise IndexError('Invalid start state')

    if end_state is not None:
        if list(range(len(end_state))) != sorted(end_state):
            raise IndexError('Invalid end state')
        num_of_zeros_end = end_state.count(0)
        if num_of_zeros_end > 1:
            raise IndexError('Invalid end state')
