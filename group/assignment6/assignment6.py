start_state = [1, 2, 0, 3]
end_state = [3, 1, 2, 0]

def move_to_lot(current_state, move_from, move_to):
    current_state[move_from], current_state[move_to] = current_state[move_to], current_state[move_from]
    return current_state

def find_empty(current_state):
    return current_state.index(0)
    
def find_car_lot(current_state, car):
    return current_state.index(car)

def compute_moves(start_state, end_state):
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
    current_state = start_state.copy()
    while current_state != end_state:
        empty = find_empty(current_state)
        right_car = end_state[empty]
        current_right_car = find_car_lot(current_state, right_car)
        current_state = move_to_lot(current_state, current_right_car, empty)
        yield (current_right_car, empty)
    
def apply_moves(start_state, moves):
    current_state = start_state.copy()
    for move in moves:
        move_from, move_to = move
        current_state = move_to_lot(current_state, move_from, move_to)
    return current_state


if __name__ == '__main__':
    #moves = compute_moves(start_state, end_state)
    #end = apply_moves(start_state, moves)
    #print(end)
    moves = compute_efficient_moves(start_state, end_state)
    end = apply_moves(start_state, moves)
    print(end)
