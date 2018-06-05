# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

import unittest

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
    
"""Function to find height of node"""
def height(node):
    
    height = 0
    temp = node
    while temp != None:
        temp = temp.parent
        height += 1
    return height

"""Function that searches for LCA of 2 given nodes in a tree"""
def lowest_common_ancestor(node1,node2):
    
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

class TestQ2(unittest.TestCase):
    
    def setUp(self):
        self.empty_tree = build_tree_from_preorder([])
        self.random_tree = build_tree_from_preorder([7,13,None,25,17,None,2])
        self.full_tree = build_tree_from_preorder(range(1,64))    
        
    def test_empty(self):
        self.assertIsNone(lowest_common_ancestor(self.empty_tree,self.empty_tree))
        
    def test_normal(self):
        self.assertEqual(lowest_common_ancestor(self.random_tree.right.right,self.random_tree.left.right),self.random_tree)
        self.assertEqual(lowest_common_ancestor(self.random_tree,self.random_tree.left),self.random_tree)
    
    def test_full(self):
        self.assertEqual(lowest_common_ancestor(self.full_tree.left.right.left.right.left,self.full_tree),self.full_tree)
        self.assertEqual(lowest_common_ancestor(self.full_tree.left.right.left.right.left,self.full_tree.left.right.left.left),self.full_tree.left.right.left)
        self.assertEqual(lowest_common_ancestor(self.full_tree.left.right.left.right.left,self.full_tree.left.left.left.left),self.full_tree.left)
        self.assertEqual(lowest_common_ancestor(self.full_tree.right.right.left.right,self.full_tree.right.right),self.full_tree.right.right)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestQ2('test_empty'))
    suite.addTest(TestQ2('test_normal'))
    suite.addTest(TestQ2('test_full'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())
        
main()
