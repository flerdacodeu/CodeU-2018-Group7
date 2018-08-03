from collections import defaultdict
from itertools import permutations
import sys


class PathFinder:
    """
    Builds a graph from all possible transitions from one parking state 
    to another. Every possible state is encoded as an integer, and these 
    integers serve as vertices of a graph. A task of finding 
    all possible sequences of moves from one state to another is then 
    translated as a task of finding all possible paths between two vertices.
    Users can specify constraints for parking spaces and the number of
    possible sequences they want to get.
    
    :param states_to_nums: dict with states encoded as integers,
                           {state: num_of_state}
    :param nums_to_states: dict with decoded integers for states,
                           {num_of_state: state}
    :param constraints: dict with constraints for parking lots,
                        {parking_lot: (list of permitted cars)}
    """
    def __init__(self, start_state, end_state, constraints=None):
        self.nums_to_states = dict()
        self.states_to_nums = dict()

        if len(start_state) != len(end_state):
            raise (ValueError, "Start and end states should have the same length")
        if constraints is None:
            length = len(start_state)
            self._constraints = {i: tuple(range(length)) for i in range(length)}
        else:
            if not constraints:
                raise (ValueError, "constraints can't be an empty dictionary")
            self._constraints = constraints
        self._start_state = start_state
        self._end_state = end_state
        self._graph = Graph()
        self._build_graph(len(start_state))

    @property
    def start_state(self):
        return self._start_state

    @start_state.setter
    def start_state(self, value):
        try:
            self._check_state_vadility(value)
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
            self._check_state_vadility(value)
            self._end_state = value
        except ValueError as e:
            print("End state doesn't satisfy constraints")
            raise e

    def _decode_path(self, path):
        """
        decodes list of paths as integers to sequences of states
        """
        return [self.nums_to_states[x] for x in path]

    @staticmethod
    def find_empty(current_state):
        """
        :returns: int, number of a currently empty lot
        """
        return current_state.index(0)

    def _check_state_validity(self, state):
        """
        Checks if the end or start state doesn't satisfy constraints and raises an error
        """
        for place_num in range(len(state)):
            if state[place_num] not in self._constraints[place_num]:
                raise ValueError

    def _build_graph(self, num_places):
        """
        Encodes all possible states as integers, builds a graph with states as vertices.
        If constraints were specified, some of the edges are not added to the graph.
        
        :param num_places: number of parking lots, required to compute permutations
        """
        graph = self._graph
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

    def find_all_paths(self, num_sequences=None):
        """
        Finds all possible paths in the graph between two vertices. Paths are returned
        as a generator. The requested number of sequences from the generator are returned.
        
        :param num_sequences: how many sequences a user wants to see, 
                              if None function returns all possible sequences
        """
        paths_generator = self._graph.find_all_paths(self.states_to_nums[self.start_state],
                                          self.states_to_nums[self.end_state])
        if num_sequences is not None:
            all_paths = list(next(paths_generator) for _ in range(num_sequences))
        else:
            all_paths = list(paths_generator)
        return [self._decode_path(path) for path in all_paths]


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def find_all_paths(self, start, end):
        nodes = [start]
        depths = [start]
        path = []
        while nodes:
            node = nodes.pop()
            level = depths.pop()
            while (len(path) > 0) and (path[-1] != level):
                path.pop()
            path.append(node)
            has_new = False
            for neighbour in self.edges[node]:
                if neighbour in path:
                    continue
                if end == neighbour:
                    new_path = path.copy()
                    new_path.append(end)
                    yield new_path
                    continue
                else:
                    has_new = True
                    nodes.append(neighbour)
                    depths.append(node)
            if not has_new:
                path.pop()

if __name__ == '__main__':
    start_state = (1, 2, 0, 3, 4, 5, 6, 7)
    end_state = (2, 1, 3, 0, 4, 5, 6, 7)
    num_sequences = 1
    path_finder = PathFinder(start_state, end_state)
    decoded_paths = path_finder.find_all_paths(num_sequences=num_sequences)
    print(decoded_paths)
