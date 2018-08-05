from collections import defaultdict
from itertools import permutations
from helpers import check_input_validity


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
    def __init__(self, start_state, end_state, constraints):

        self._nums_to_states = dict()
        self._states_to_nums = dict()
        self._constraints = constraints
        self._graph = Graph()
        self._build_graph(len(start_state))
        self.start_state = start_state
        self.end_state = end_state

    @property
    def start_state(self):
        return self._start_state

    @start_state.setter
    def start_state(self, value):
        check_input_validity(start_state=value)
        try:
            self._check_state_validity(value)
            self._start_state = value
        except ValueError as e:
            print("Start state doesn't satisfy constraints")
            raise e

    @property
    def end_state(self):
        return self._end_state

    @end_state.setter
    def end_state(self, value):
        check_input_validity(end_state=value)
        try:
            self._check_state_validity(value)
            self._end_state = value
        except ValueError as e:
            print("End state doesn't satisfy constraints")
            raise e

    def decode_path(self, path):
        """
        Decodes list of paths as integers to sequences of states
        """
        return [self._nums_to_states[x] for x in path]

    @staticmethod
    def find_empty(current_state):
        """
        Assumes that empty lot is equal 0
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
        self._nums_to_states = dict(enumerate(map(list, all_permutations)))
        self._states_to_nums = {tuple(state): num for num, state in self._nums_to_states.items()}
        graph.vertices = self._nums_to_states.keys()
        for num in graph.vertices:
            state = self._nums_to_states[num]
            empty = self.find_empty(state)
            for i in range(num_places):
                if i != empty:
                    new_state = state.copy()
                    if len(self._constraints) > 0:
                        if new_state[i] not in self._constraints[i]:
                            continue
                    new_state[empty], new_state[i] = new_state[i], new_state[empty]
                    graph.edges[num].append(self._states_to_nums[tuple(new_state)])

    def find_all_paths(self):
        """
        Finds all possible paths in the graph between two vertices. Paths are returned
        as a generator
        """
        if not self.start_state:
            return []
        return self._graph.find_all_paths(self._states_to_nums[self.start_state],
                                          self._states_to_nums[self.end_state])


class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def find_all_paths(self, start, end):
        """
        Finds all possible paths from the start vertex to the end
        Algorithm is iterative to avoid recursion stack limitations
        """
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
