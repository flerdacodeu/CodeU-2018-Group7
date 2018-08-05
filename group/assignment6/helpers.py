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
    empty_lot = start_state.index(0)
    car = end_state[empty_lot]
    move_from = start_state.index(car)
    return (move_from, empty_lot)
