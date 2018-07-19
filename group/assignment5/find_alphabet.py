"""
Find the alphabet on the given dictionary + identify inconsistent dictionaries
"""

from typing import List
from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.vertices = set()

    def add_edge(self, u, v):
        self.adjacency_list[u] = v
        self.vertices.add(u)
        self.vertices.add(v)


def create_graph(dictionary):
    graph = Graph()

    # go through the dict and compare pairs of words:
    # one by one compare characters and add to the graph edge f->s and break
    # where f and s - first non-equal characters from the comparing pair
    for i in range(len(dictionary)-1):
        first_word = dictionary[i]
        second_word = dictionary[i+1]
        for first_ch, second_ch in zip(first_word, second_word):
            if first_ch != second_ch:
                graph.add_edge(first_ch, second_ch)
                break
    return graph


def find_alphabet(dictionary: List[str]):
    """
    finds the alphabet by the given dictionary
    :param dictionary: List of words
    :returns: List of characters or None if the given dictionary is inconsistent
    """

    # create graph from the given dictionary
    graph = create_graph(dictionary)
    # return the characters in topological order as the requirement alphabet
    if graph.vertices:
        result = topological_sort(graph, list(graph.vertices)[0])
        if result is None:
            raise BaseException("The given dictionary is inconsistent")
        return result
    return []


def dfs(graph, v, visited, order):
    # visited - array of marks for every vertex
    # visited[v] = 0 - v hasn't been visited yet
    #              1 - visited but haven't visited all vertices in it's subtree
    #              2 - all vertices in it's subtree were visited
    visited[v] = 1
    graph_list = graph.adjacency_list
    for neighbour in graph_list[v]:

        # neighbour hasn't been visited yet
        if not visited[neighbour]:
            dfs(graph, neighbour, visited, order)

        # cycle was found => no topological sort
        elif visited[neighbour] == 1:
            return False
    visited[v] = 2
    order.appendleft(v)
    return True


def topological_sort(graph, v):
    """
    :returns: None if there is no topological sort
    or the list of vertices in topological sort order
    """
    visited = dict.fromkeys(graph.vertices, 0)
    order = deque()

    # go through all vertices and run the updated dfs
    # if there is a cycle in the given graph => raise Error and return None
    for v in graph.vertices:
        if not visited[v]:
            if not dfs(graph, v, visited, order):
                return None
    return list(order)