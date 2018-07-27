from collections import defaultdict
from itertools import permutations
import sys


class Graph:
    """
    Args:
        nums_to_states: {num_of_state: state}
        states_to_nums: {state: num_of_state}
    """
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
        self.nums_to_states = dict()
        self.states_to_nums = dict()

    def add_edge(self, u, v):
        self.edges[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)

    def print_all_paths(self, start, end, visited=None, path=None, all_paths=None):
        if visited is None:
            visited = [False]*(len(self.vertices))
        if path is None:
            path = []
        if all_paths is None:
            all_paths = []

        visited[start] = True
        path.append(start)

        if start == end:
            all_paths.append([self.nums_to_states[x] for x in path])
        else:
            for i in self.edges[start]:
                if not visited[i]:
                    self.print_all_paths(i, end, visited, path, all_paths)

        path.pop()
        visited[start] = False
        return all_paths

    
    def find_all_paths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.edges[start]:
            if node not in path:
                newpaths = self.find_all_paths(node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths
    
    def decode_path(self, path):
        return [self.nums_to_states[x] for x in path]

def find_empty(current_state):
    """
    :returns: int, number of a currently empty lot
    """
    return current_state.index(0)


def build_graph(num_places, constraints={}):
    graph = Graph()
    all_permutations = permutations(range(num_places))
    graph.nums_to_states = dict(enumerate(map(list, all_permutations)))
    graph.states_to_nums = {tuple(state): num for num, state in graph.nums_to_states.items()}
    graph.vertices = graph.nums_to_states.keys()
    for num in graph.vertices:
        state = graph.nums_to_states[num]
        empty = find_empty(state)
        for i in range(num_places):
            if i != empty:
                new_state = state.copy()
                if len(constraints) > 0:
                    if new_state[i] not in constraints[i]:
                        continue
                new_state[empty], new_state[i] = new_state[i], new_state[empty]
                graph.edges[num].append(graph.states_to_nums[tuple(new_state)])

    return graph

if __name__ == '__main__':
    start_state = (1, 2, 0, 3)
    end_state = (3, 1, 2, 0)
    constraints = {0: (0, 1, 2, 3), 1: (0, 1, 2), 2: (0, 1, 3), 3: (0, 1, 2, 3)}
    g = build_graph(4, constraints)
    my_paths = g.find_all_paths(g.states_to_nums[start_state], g.states_to_nums[end_state])
    decoded_paths = [g.decode_path(path) for path in my_paths]
    print(decoded_paths)
    old_paths =  g.print_all_paths(g.states_to_nums[start_state], g.states_to_nums[end_state])
    print(len(my_paths), len(old_paths))
