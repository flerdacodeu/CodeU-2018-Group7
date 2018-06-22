#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 13:44:29 2018

@author: user
"""

import unittest
from assignment3 import create_grid,find_words_from_grid
from dictionary import Dictionary

class TestQ2(unittest.TestCase):
    
    def setUp(self):
        self.empty_dictionary = Dictionary([])
        self.dictionary1 = Dictionary(['ana','ema','eganam'])
        self.dictionary2 = Dictionary(['ana','ema','ama','ame'])
        self.grid = create_grid(3,3,['e','m','a','g','a','n','g','g','g'])   
        self.word = ""
        self.foundWords = set()
        self.visited = {}
        for x in range(0, 3):
            for y in range(0, 3):
                self.visited[(x, y)] = 0
        
    def test_empty(self):
        find_words_from_grid(self.grid,0,0,3,3,self.empty_dictionary,self.foundWords)
        self.assertEqual(set(),self.foundWords)
        
    def test_normal(self):
        find_words_from_grid(self.grid,0,0,3,3,self.dictionary1,self.foundWords)
        self.assertEqual(set(['ema','ema','eganam']),self.foundWords)
        self.foundWords.clear();
        find_words_from_grid(self.grid,0,2,3,3,self.dictionary2,self.foundWords)
        self.assertEqual(set(['ana','ama','ame']),self.foundWords)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestQ2('test_empty'))
    suite.addTest(TestQ2('test_normal'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())
        
main()
