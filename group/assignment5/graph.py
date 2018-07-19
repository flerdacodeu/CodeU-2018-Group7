from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)


def build_graph(dictionary):
    """Given a lexicographically ordered list of words compares pairs of subsequent words and
    adds an edge f -> s in a graph if letter f is lexicographically smaller than s
    """
    graph = Graph()
    for i in range(len(dictionary)-1):
        first_word = dictionary[i]
        second_word = dictionary[i+1]
        for first_ch, second_ch in zip(first_word, second_word):
            if first_ch != second_ch:
                graph.add_edge(first_ch, second_ch)
                break
    return graph
