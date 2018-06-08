# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

#If we assume that we can have a pointer to the parent
class TreeNode:
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = left
        self.parent = parent
        

def build_tree_from_preorder(values):
    """Function to build tree from preorder that contains None pointers where needed"""    
    
    if len(values) == 0 or values[0] == None:
        return None
    root = TreeNode(values[0])
    if len(values) == 1:
        return root
    root.left = build_tree_from_preorder(values[1:((len(values)-1) // 2 + 1)])
    root.right = build_tree_from_preorder(values[((len(values)-1) // 2 + 1):]) 
    if root.left != None:
        root.left.parent = root
    if root.right != None:
        root.right.parent = root
    
    return root

def find_ancestors(node):
    """We just go through pointers to parent until we reach None"""    
    
    result = []
    if node == None:
        return None
    temp = node
    while temp.parent != None:
        result.append(temp.parent.val)
        temp = temp.parent
    return result

def height(node):
    """Function to find height of node"""
    
    height = 0
    temp = node
    while temp != None:
        temp = temp.parent
        height += 1
    return height

def lowest_common_ancestor(node1,node2):
    """Function that searches for LCA of 2 given nodes in a tree"""
    
    height1 = height(node1)
    height2 = height(node2)
    
    temp1 = node1
    temp2 = node2
    
    if height1 > height2:
        for i in range(0,height1-height2):
            temp1 = temp1.parent
    else:
        for i in range(0,height2-height1):
            temp2 = temp2.parent
            
    while temp1 != temp2:
        temp1 = temp1.parent
        temp2 = temp2.parent
    
    return temp1
