from graph import Graph

def extract_rule(first_string, second_string):
    """
    Given two strings where first string is lexicographically less than second extracts a rule
    between two symbols so that a symbol from the first string is lexicographically lower than
    a symbol from the second string
    """
    i = 0
    while ((i < min(len(first_string), len(second_string))) and
           (first_string[i] == second_string[i])):
        i += 1

    if i == min(len(first_string), len(second_string)):
        return None
    return (first_string[i], second_string[i])

def extract_all_rules(dictionary):
    #rules = list()
    for i in range(1, len(dictionary)):
        rule = extract_rule(dictionary[i - 1], dictionary[i])
        if rule:
            yield rule

def compute_alphabet(dictionary):
    """
    Given a lexicographically ordered list of words computes a valid alphabet if the dictionary is
    consistent. Otherwise, raises an error
    """
    rules = extract_all_rules(dictionary)
    graph = Graph()
    for word in dictionary:
        for symbol in word:
            graph.add_vertex(symbol)
    for rule in rules:
        graph.add_edge(rule[1], rule[0])
    try:
        alphabet = graph.topological_sort()
    except:
        raise ValueError("Dictionary is incosistent")
    return alphabet
