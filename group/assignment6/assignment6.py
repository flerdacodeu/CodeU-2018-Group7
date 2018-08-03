"""
There is a parking lot with N spaces and N-1 cars in it. Below is 
an algorithm to rearrange the cars in a given way. Only one car can be 
moved at a time to the empty slot. Start state and end state are 
represented as lists of car numbers, and 0 signifies empty slot. 
Thus, a number of a lot in which a car is placed is an index of that car
number in the list. For example, [1, 2, 0, 3] is the start state. 
Car #1 is in the lot #0, car #2 is in the lot #1, etc.
"""
from path_finder import PathFinder
if __name__ == '__main__':
    start_state = [1, 2, 0, 3] 
    end_state = [3, 1, 2, 0]
    path_finder = PathFinder(start_state, end_state)
    moves = list(path_finder.compute_efficient_moves())
    print(moves)
    print(path_finder.apply_moves(moves))
