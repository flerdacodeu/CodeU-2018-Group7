'''
There is a parking lot with N spaces and N-1 cars in it. Below is 
an algorithm to rearrange the cars in a given way. Only one car can be 
moved at a time to the empty slot. Start state and end state are 
represented as lists of car numbers, and 0 signifies empty slot. 
Thus, a number of a lot in which a car is placed is an index of that car
number in the list. For example, [1, 2, 0, 3] is the start state. 
Car #1 is in the lot #0, car #2 is in the lot #1, etc.
'''

def move_to_lot(current_state, move_from, move_to):
    '''
    Move a car from one slot to another. As we are always moving a car to
    an empty slot, the function basically swaps an empty and occupied slots.

    :param current_state: order of cars in the present moment
    :param move_from: int, number of a lot from which the car is moved
    :param move_to: int, number of an empty slot to which we move the car
    :returns: modified current state
    '''
    current_state[move_from], current_state[move_to] = current_state[move_to], \
                                                       current_state[move_from]
    return current_state

def find_empty(current_state):
    ''' 
    :returns: int, number of a currently empty lot
    '''
    return current_state.index(0)
    
def find_car_lot(current_state, car):
    ''' 
    :returns: int, number of a lot in which a given car is currently placed
    '''
    return current_state.index(car)

def compute_moves(start_state, end_state):
    '''
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
    '''
    if len(start_state) != len(end_state):
        raise IndexError('The start state and end state have different lengths.')
    current_state = start_state.copy()
    for lot in range(len(current_state)):
        right_car = end_state[lot]
        current_right_car = find_car_lot(current_state, right_car)
        if not current_state[lot] == 0:
            empty = find_empty(current_state)
            current_state = move_to_lot(current_state, lot, empty)
            yield (lot, empty)
        current_state = move_to_lot(current_state, current_right_car, lot)
        yield (current_right_car, lot)
        if current_state == end_state:
            break    
    
def compute_efficient_moves(start_state, end_state):
    '''
    More efficiently omputes a sequence of moves that are required to rearrange cars
    from the given start state to the end state.
    We look up which lot is empty and which car should be in this slot.
    Then we move the required car to the empty lot and repeat the procedure.

    :param start_state: order of cars in the start of the rearrangement
    :param end_state: order of cars after rearrangement
    :yields: move steps. Each move is represented as a tuple with two indeces,
             the 1st index is the number of lot from which we move the car,
             the 2nd index is the number of lot to which we move the car
    '''
    if len(start_state) != len(end_state):
        raise IndexError('The start state and end state have different lengths.')
    current_state = start_state.copy()
    while current_state != end_state:
        empty = find_empty(current_state)
        right_car = end_state[empty]
        current_right_car = find_car_lot(current_state, right_car)
        current_state = move_to_lot(current_state, current_right_car, empty)
        yield (current_right_car, empty)
    
def apply_moves(start_state, moves):
    '''
    Function for checking the correctness of our results. We take 
    the start state and apply the move steps.
    
    :param start_state: order of cars in the start of the rearrangement
    :param moves: generator, sequence of moves that we need to apply.
                  Each move is represented as a tuple with two indeces, 
                  the 1st index is the number of lot from which we move the car,
                  the 2nd index is the number of lot to which we move the car
    :returns: end state, list of car numbers. 
    '''
    current_state = start_state.copy()
    for move in moves:
        move_from, move_to = move
        current_state = move_to_lot(current_state, move_from, move_to)
    return current_state


if __name__ == '__main__':
    start_state = [1, 2, 0, 3]
    end_state = [3, 1, 2, 0]
    moves = compute_efficient_moves(start_state, end_state)
    print(apply_moves(start_state, moves))
