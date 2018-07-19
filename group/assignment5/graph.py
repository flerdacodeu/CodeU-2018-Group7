from collections import defaultdict


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
