#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

import unittest
from assignment4 import count_islands

class Test(unittest.TestCase):
    
    def setUp(self):
        self.tiles_empty = []
        self.tiles1 = [[False,False],[False,False]]
        self.tiles2 = [[True,True]]
        self.tiles3 = [[True,True,True,True,True],[True,False,False,False,True],[True,False,True,False,True],[True,False,False,False,True],[True,True,True,True,True]]
        
    def test_empty(self):
        self.assertEqual(0,count_islands(0,0,self.tiles_empty))
    
    def test_small(self):
        self.assertEqual(0,count_islands(2,2,self.tiles1))
        self.assertEqual(1,count_islands(1,2,self.tiles2))
        
    def test_bigger(self):
        self.assertEqual(2,count_islands(5,5,self.tiles3))
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(Test('test_empty'))
    suite.addTest(Test('test_small'))
    suite.addTest(Test('test_bigger'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    
main()