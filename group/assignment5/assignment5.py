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

def topsort(lettersGraph):
    #topological sort of graph that returns one valid solution
    alphabet = []
    queue = []
    for letter in lettersGraph:
        if lettersGraph[letter].get_number_of_parents() == 0:
            queue.append(lettersGraph[letter])
    
    i = 0
    qlen = len(queue)
    while i < qlen:
        alphabet.append(queue[i].get_data())
        children = queue[i].get_children()
        for child in children:
            lettersGraph[child].remove_parent()
            if lettersGraph[child].get_number_of_parents() == 0:
                queue.append(lettersGraph[child])
                qlen += 1
        i += 1
    """if dictionary is consistent we will go through all lettersGraph,
    so if we haven't done that dictionary is inconsistent
    """
    if qlen < len(lettersGraph):
        raise BaseException("The given dictionary is inconsistent")
    return alphabet

def find_alphabet(dictionary):
    """finds alphabet of given dictionary.It will return just one of the valid dictionaries.
    This function created directed graph where nodes are lettersGraph and edges are relations between lettersGraph
    (edge from a to b means that a is before b)
    """
    lettersGraph = {}
    numOfWords = len(dictionary)
    
    #creating graph node for every letter that exists in dictionary
    for word in dictionary:
        for i in range(0,len(word)):
            if not (word[i] in lettersGraph):
                lettersGraph[word[i]] = GraphNode(word[i])
           
    #adding edges to graph 
    for i in range (1,numOfWords):
        j = find_first_different_letter(dictionary[i-1],dictionary[i])
        if j != -1:
            lettersGraph[dictionary[i-1][j]].add_child(dictionary[i][j])
            lettersGraph[dictionary[i][j]].add_parent()
            
    return topsort(lettersGraph)
        
def main():
    
    dictionary = []
    n = int(input())
    for i in range(0,n):
        word = input()
        dictionary.append(word)
    alphabet = find_alphabet(dictionary)
    print(alphabet)

    
