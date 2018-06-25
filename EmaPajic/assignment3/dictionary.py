#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: user
"""

class Dictionary:
    
    def __init__(self, words = set()):
        self.words = words
        
    def add(self, word):
        if word in self.words:
            return
        self.words.add(word)
        
    def is_word(self, word):
        return word in self.words
    
    def is_prefix(self,prefix):
        for word in self.words:
            if word.startswith(prefix):
                return True     
        return False