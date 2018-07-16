#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""
from Graph import GraphNode

def find_first_different_letter(word1, word2):
    """returns position in words of first different letter,
    -1 is words are same (or atleast same until the end of the shorter word)
    """
    i = 0
    while i < len(word1) and i < len(word2):
        if word1[i] != word2[i]:
            return i
        i += 1
    return -1

def topsort(letters_graph):
    #topological sort of graph that returns one valid solution
    alphabet = []
    q = queue.Queue()
    for letter in letters_graph:
        if letters_graph[letter].get_number_of_parents() == 0:
            q.put(letters_graph[letter])
    
    num_of_visited_letters = 0
    while not q.empty():
        curr_letter = q.get()
        num_of_visited_letters += 1
        alphabet.append(curr_letter.get_data())
        children = curr_letter.get_children()
        for child in children:
            letters_graph[child].remove_parent()
            if letters_graph[child].get_number_of_parents() == 0:
                q.put(letters_graph[child])
    """if dictionary is consistent we will go through all letters_graph,
    so if we haven't done that dictionary is inconsistent
    """
    if num_of_visited_letters < len(letters_graph):
        raise BaseException("The given dictionary is inconsistent")
    return alphabet

def find_alphabet(dictionary):
    """finds alphabet of given dictionary.
    It will return just one of the valid dictionaries.
    This function created directed graph where nodes are letters_graph
    and edges are relations between letters_graph
    (edge from a to b means that a is before b)
    """
    letters_graph = {}
    numOfWords = len(dictionary)
    
    #creating graph node for every letter that exists in dictionary
    for word in dictionary:
        for i in range(0,len(word)):
            if not (word[i] in letters_graph):
                letters_graph[word[i]] = GraphNode(word[i])
           
    #adding edges to graph 
    for i in range (1,numOfWords):
        j = find_first_different_letter(dictionary[i-1],dictionary[i])
        if j != -1:
            letters_graph[dictionary[i-1][j]].add_child(dictionary[i][j])
            letters_graph[dictionary[i][j]].add_parent()
            
    return topsort(letters_graph)
        
def main():
    
    dictionary = []
    n = int(input())
    for i in range(0,n):
        word = input()
        dictionary.append(word)
    alphabet = find_alphabet(dictionary)
    print(alphabet)
    
