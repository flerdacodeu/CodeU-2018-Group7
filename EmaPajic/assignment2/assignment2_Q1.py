#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""
import unittest

"""If we assume that we can have a pointer to the parent"""

class TreeNode:
    def __init__(self, val, left = None, right = None, parent = None):
        self.val = val
        self.left = left
        self.right = left
        self.parent = parent
        
"""We just go through pointers to parent until we reach None"""
def find_ancestors(node):
    
    result = []
    if node == None:
        return None
    temp = node
    while temp.parent != None:
        result.append(temp.parent.val)
        temp = temp.parent
    return result

"""Function to build tree from preorder that contains None pointers where needed"""
def build_tree_from_preorder(values):
    
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

class TestQ1(unittest.TestCase):
    
    def setUp(self):
        self.empty_tree = build_tree_from_preorder([])
        self.random_tree = build_tree_from_preorder([7,13,None,25,17,None,2])
        self.full_tree = build_tree_from_preorder(range(1,64))    
        
    def test_empty(self):
        self.assertIsNone(find_ancestors(self.empty_tree))
        
    def test_normal(self):
        self.assertEqual(find_ancestors(self.random_tree.right.right),[17,7])
        self.assertEqual(find_ancestors(self.random_tree),[])
    
    def test_full(self):
        self.assertEqual(find_ancestors(self.full_tree.left.right.left.right.left),[23,19,18,2,1])

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestQ1('test_empty'))
    suite.addTest(TestQ1('test_normal'))
    suite.addTest(TestQ1('test_full'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())
        
main()