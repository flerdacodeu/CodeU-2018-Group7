#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

import unittest
from assignment5 import find_alphabet

class TestQ5(unittest.TestCase):
      
    def setUp(self):
        self.empty_dictionary = []
        self.dictionary1 = ['ART','RAT','CAT','CAR']
        
    def test_empty(self):
        self.assertEqual([],find_alphabet(self.empty_dictionary))
        
    def test_normal(self):
        self.assertIn(find_alphabet(self.dictionary1),[['A','T','R','C'],
                                                      ['T','A','R','C']])
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestQ5('test_empty'))
    suite.addTest(TestQ5('test_normal'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())
        
main()