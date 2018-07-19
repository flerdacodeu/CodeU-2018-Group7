from typing import List
from collections import deque
from assignment5.graph import build_graph


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


def find_alphabet(dictionary: List[str]):
    """
    finds the alphabet by the given dictionary
    :param dictionary: List of words
    :returns: List of characters or None if the given dictionary is inconsistent
    """
    graph = build_graph(dictionary)
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

    for v in graph.vertices:
        if not visited[v]:
            if not dfs(graph, v, visited, order):
                return None
    return list(order)
