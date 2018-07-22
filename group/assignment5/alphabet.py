from collections import defaultdict
from graph import Graph

def extract_rule(first_string, second_string):
    """
    Given two strings where first string is lexicographically less than second extracts a rule
    between two symbols so that a symbol from the first string is lexicographically lower than
    a symbol from the second string
    """
    i = 0
    while (i < min(len(first_string), len(second_string)) and
           first_string[i] == second_string[i]):
        i += 1

    if i == min(len(first_string), len(second_string)):
        return None
    return (first_string[i], second_string[i])

def extract_all_rules(dictionary):
    for i in range(1, len(dictionary)):
        rule = extract_rule(dictionary[i - 1], dictionary[i])
        if rule is not None:
            yield rule

def build_graph(dictionary):
    rules = extract_all_rules(dictionary)
    graph = Graph()
    for word in dictionary:
        for symbol in word:
            graph.add_vertex(symbol)
    for rule in rules:
        graph.add_edge(rule[1], rule[0])
    return graph

def compute_alphabet(dictionary):
    """
    Given a lexicographically ordered list of words computes a valid alphabet if the dictionary is
    consistent. Otherwise, raises an error
    """
    graph = build_graph(dictionary)
    try:
        alphabet = graph.topological_sort()
    except:
        raise ValueError("Dictionary is incosistent")
    return alphabet

def compute_all_alphabets(dictionary):
    graph = build_graph(dictionary)
    letters = graph.vertices
    letters_to_add = list()
    added_children = defaultdict(int)
    all_alphabets = list()
    for l in letters:
        if len(graph.edges[l]) == 0:
            letters_to_add.append(l)
    compute_all_alphabets_with_prefix(graph, '', letters_to_add, added_children,
            all_alphabets)
    return set(all_alphabets)


def compute_all_alphabets_with_prefix(graph, prefix, letters_to_add, added_children,
        all_alphabets):
    if len(prefix) == len(graph.vertices):
        all_alphabets.append(prefix)
        return
    if len(letters_to_add) == 0:
        return
    for l in letters_to_add:
        prefix_new = prefix + l
        added_children_new = added_children.copy()
        letters_to_add_new = letters_to_add.copy()
        letters_to_add_new.remove(l)
        parents = graph.parents[l]
        for p in parents:
            added_children_new[p] += 1
            # if we added all children of p then we add p into letters_to_add
            if added_children_new[p] == len(graph.edges[p]): #and (not p in prefix_new):
                letters_to_add_new.append(p)
        compute_all_alphabets_with_prefix(graph, prefix_new, letters_to_add_new,
                added_children_new, all_alphabets)
