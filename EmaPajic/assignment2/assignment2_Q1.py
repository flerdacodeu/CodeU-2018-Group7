#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""
import unittest
import assignments

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
