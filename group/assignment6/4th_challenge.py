from collections import defaultdict
from itertools import permutations
import sys


class Parking:
    """
    Args:
        nums_to_states: {num_of_state: state}
        states_to_nums: {state: num_of_state}
        constraints: {parking_lot: (permitted cars)}
    """
    def __init__(self):
        self.nums_to_states = dict()
        self.states_to_nums = dict()
        self.constraints = set()

    def decode_path(self, path):
        return [self.nums_to_states[x] for x in path]

    def find_empty(self, current_state):
        """
        :returns: int, number of a currently empty lot
        """
        return current_state.index(0)

    def check_state(self, start_state, end_state):
        for place_num in range(len(start_state)):
            if start_state[place_num] not in self.constraints[place_num]:
                raise ValueError("Start state doesn't satisfy constraints")
                return False
            if end_state[place_num] not in self.constraints[place_num]:
                raise ValueError("End state doesn't satisfy constraints")
                return False
        return True

    def build_graph(self, num_places):
        graph = Graph()
        all_permutations = permutations(range(num_places))
        self.nums_to_states = dict(enumerate(map(list, all_permutations)))
        self.states_to_nums = {tuple(state): num for num, state in self.nums_to_states.items()}
        graph.vertices = self.nums_to_states.keys()
        for num in graph.vertices:
            state = self.nums_to_states[num]
            empty = self.find_empty(state)
            for i in range(num_places):
                if i != empty:
                    new_state = state.copy()
                    if len(self.constraints) > 0:
                        if new_state[i] not in self.constraints[i]:
                            continue
                    new_state[empty], new_state[i] = new_state[i], new_state[empty]
                    graph.edges[num].append(self.states_to_nums[tuple(new_state)])

        return graph

class Graph:

    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def find_all_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.edges[start]:
            if node not in path:
                new_paths = self.find_all_paths(node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths


if __name__ == '__main__':
    start_state = (1, 2, 0, 3)
    #end_state = (2, 1, 3, 0)
    end_state = (3, 1, 2, 0)
    parking = Parking()
    parking.constraints = {0: (0, 1, 2, 3), 1: (0, 1, 2), 2: (0, 1, 3), 3: (0, 1, 2, 3)}
    g = parking.build_graph(4)
    if parking.check_state(start_state, end_state):
        my_paths = g.find_all_paths(parking.states_to_nums[start_state],\
                                    parking.states_to_nums[end_state])
        decoded_paths = [parking.decode_path(path) for path in my_paths]
        print(decoded_paths)
