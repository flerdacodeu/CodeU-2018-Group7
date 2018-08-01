from collections import defaultdict
from itertools import permutations
import sys


class PathFinder:
    """
    Args:
        nums_to_states: {num_of_state: state}
        states_to_nums: {state: num_of_state}
        constraints: {parking_lot: (permitted cars)}
    """
    def __init__(self, start_state, end_state, constraints):
        assert len(start_state) == len(end_state), "Start and end states have different length"
        self.nums_to_states = dict()
        self.states_to_nums = dict()
        self._constraints = constraints
        self.start_state = start_state
        self.end_state = end_state
        self.graph = Graph()
        self.build_graph(len(start_state))

    @property
    def start_state(self):
        return self._start_state

    @start_state.setter
    def start_state(self, value):
        try:
            self.check_state(value)
            self._start_state = value
        except ValueError as e:
            print("Start state doesn't satisfy constraints")
            raise e

    @property
    def end_state(self):
        return self._end_state

    @end_state.setter
    def end_state(self, value):
        try:
            self.check_state(value)
            self._end_state = value
        except ValueError as e:
            print("End state doesn't satisfy constraints")
            raise e

    def decode_path(self, path):
        return [self.nums_to_states[x] for x in path]

    def find_empty(self, current_state):
        """
        :returns: int, number of a currently empty lot
        """
        return current_state.index(0)

    def check_state(self, state):
        for place_num in range(len(state)):
            if state[place_num] not in self._constraints[place_num]:
                raise ValueError

    def build_graph(self, num_places):
        graph = self.graph
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
                    if len(self._constraints) > 0:
                        if new_state[i] not in self._constraints[i]:
                            continue
                    new_state[empty], new_state[i] = new_state[i], new_state[empty]
                    graph.edges[num].append(self.states_to_nums[tuple(new_state)])

    def find_all_paths(self):
        return self.graph.find_all_paths(self.states_to_nums[self.start_state],\
                                         self.states_to_nums[self.end_state])


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
    end_state = (2, 1, 3, 0)
    #end_state = (3, 1, 2, 0)

    path_finder = PathFinder(start_state, end_state, constraints={0: (0, 1, 2, 3), 1: (0, 1, 2), 2: (0,
        1, 3), 3: (0, 1, 2, 3)})
    my_paths = path_finder.find_all_paths()
    decoded_paths = [path_finder.decode_path(path) for path in my_paths]
    print(decoded_paths)
