#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

class GraphNode:
    """for each graph node we have it's data (letter in this case),
    number of parents (we need that for topsort) and set of children.
    We just need number of parents since all parent-child relationships
    are stored in children set
    """
    
    def __init__(self, data, num_of_parents = 0):
        self.data = data
        self.num_of_parents = num_of_parents
        self.children = set()
        
    def __hash__(self):
        return hash((self.data))
        
    def get_data(self):
        return self.data
    
    def get_children(self):
        return self.children
    
    def get_number_of_parents(self):
        return self.num_of_parents
    
    def add_child(self,child):
        if not (child in self.children):
            self.children.add(child)
            
    def add_parent(self):
        self.num_of_parents += 1
    
    def remove_parent(self):
        self.num_of_parents -= 1
