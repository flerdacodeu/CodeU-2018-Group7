from typing import List
from assignment5.graph import *


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
        result = graph.topological_sort(list(graph.vertices)[0])
        if result is None:
            raise BaseException("The given dictionary is inconsistent")
        return result
    return []
