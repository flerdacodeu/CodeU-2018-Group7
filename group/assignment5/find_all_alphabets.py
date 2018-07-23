from assignment5.graph import *
from assignment5.find_alphabet import build_graph


def find_all_alphabets(dictionary):
    graph = build_graph(dictionary)
    letters = graph.vertices
    letters_to_add = list()
    added_parents = defaultdict(int)
    all_alphabets = list()
    for l in letters:
        if len(graph.parents[l]) == 0:
            letters_to_add.append(l)
    find_all_alphabets_with_prefix(graph, '', letters_to_add, added_parents,
                                   all_alphabets)
    return set(all_alphabets)


def find_all_alphabets_with_prefix(graph, prefix, letters_to_add, added_parents,
                                   all_alphabets):
    if len(prefix) == len(graph.vertices):
        all_alphabets.append(prefix)
        return
    if len(letters_to_add) == 0:
        return
    for l in letters_to_add:
        prefix_new = prefix + l
        added_parents_new = added_parents.copy()
        letters_to_add_new = letters_to_add.copy()
        letters_to_add_new.remove(l)
        children = graph.adjacency_list[l]
        for c in children:
            added_parents_new[c] += 1
            # if we added all parents of p then we add p into letters_to_add
            if added_parents_new[c] == len(graph.parents[c]): #and (not p in prefix_new):
                letters_to_add_new.append(c)
        find_all_alphabets_with_prefix(graph, prefix_new, letters_to_add_new,
                                       added_parents_new, all_alphabets)
