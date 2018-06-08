# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

import unittest
from assignments import TreeNode,build_tree_from_preorder,height,lowest_common_ancestor

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
