"""
-Find the alphabet on the given dictionary + identify inconsistent dictionaries
 and return minimal set of constraints
"""
from typing import List
from itertools import combinations
from assignment5.graph import *


def word_is_consistent(word):
    """
    Checks if we need to remove word or not
    """
    return True


def build_graph(dictionary):
    """
    Given a lexicographically ordered list of words compares pairs of subsequent words and
    adds an edge f -> s in a graph if letter f is lexicographically smaller than s
    """
    graph = Graph()
    graph.vertices = {vertex for word in dictionary for vertex in word}
    for i in range(len(dictionary)-1):
        first_word = dictionary[i]
        second_word = dictionary[i+1]
        for first_ch, second_ch in zip(first_word, second_word):
            if first_ch != second_ch:
                graph.add_edge(first_ch, second_ch)
                break
    return graph


def find_alphabet_dictionary_constraints(dictionary: List[str]):
    """
    Finds the alphabet, consistent dictionary and
     minimal set of constraints by the given dictionary
    :param dictionary: List of words
    :returns: (alphabet, consistent dictionary, minimal set of constraints)
    """

    alphabet, new_dictionary, words_to_remove = [], dictionary, set()

    # try to build alphabet from the input dictionary
    # then if it is inconsistent try to remove every
    # word and build the alphabet again then every 2 words etc
    for i in range(len(dictionary)):
        combinations_words = combinations(dictionary, i)
        for words_to_remove in combinations_words:
            new_dictionary = [word for word in dictionary
                              if word not in words_to_remove
                              and word_is_consistent(word)]
            graph = build_graph(new_dictionary)
            if graph.vertices:
                alphabet = graph.topological_sort(list(graph.vertices)[0])
                if alphabet is not None:
                    return alphabet, new_dictionary, set(words_to_remove)
    return alphabet, new_dictionary, words_to_remove


def find_alphabet(dictionary: List[str]):
    """
    :returns: alphabet (which is built on the maximal consistent dictionary)
    """
    return find_alphabet_dictionary_constraints(dictionary)[0]


def find_dictionary(dictionary: List[str]):
    """
    :returns: maximal subset of dictionary which is consistent
    """
    return find_alphabet_dictionary_constraints(dictionary)[1]


def find_constraints(dictionary: List[str]):
    """
    :returns: minimal set of constraints
    """
    return find_alphabet_dictionary_constraints(dictionary)[2]
