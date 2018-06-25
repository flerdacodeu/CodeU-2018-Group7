#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

from dictionary import Dictionary

def out_of_bounds(grid,i,j,n,m,visited):
    #checks if coordinates are out of bounds or if it is already visited
    if i < 0 or j < 0:
        return True
    if i >= n or j>= m:
        return True
    if visited[tuple((i,j))] == 1:
        return True
    return False

def find_words_from_grid(grid,i,j,n,m,dictionary,found_words,word = None,visited = None):
    #function that finds all words from grid that are in dictionary and returns them in set, i and j are starting positions of search, word is our current word found
    if word is None:
        word = ""
    if visited is None:
        visited = {}
        for x in range(0, n):
            for y in range(0, m):
                visited[(x, y)] = 0
    
    if out_of_bounds(grid,i,j,n,m,visited):
        return
    word += grid[i][j]
    visited[tuple((i,j))] = 1
    if dictionary.is_word(word):
        found_words.add(word)
    elif dictionary.is_prefix(word):
        for i1 in range(-1,2):
            for j1 in range(-1,2):
                find_words_from_grid(grid,i+i1,j+j1,n,m,dictionary,found_words,word,visited)
    visited[tuple((i,j))] = 0


def create_grid(n,m,inputs):
    #function that creates grid from given values
    grid = [0] * n
    for i in range(n):
        grid[i] = [0] * m
    
    temp = 0
    for i in range(0,n):
        for j in range(0,m):
            grid[i][j] = inputs[temp]
            temp += 1
            
    return grid
        
        
def main():
    #main function if we want to check something that is not in the tests
    print('Input the number of words in dictionary')
    nd = int(input())
    print('Input the words')
    inputsdict = [0]*nd
    for i in range(0,nd):
        inputsdict[i] = input()
    
    print('Input the number of rows and columns')
    n = int(input())
    m = int(input())
    print('Input the letters')
    inputsgrid = [0]*(n*m)
    for i in range(0,n*m):
        inputsgrid[i] = input()
        
    dictionary = Dictionary(inputsdict)
    grid = create_grid(n,m,inputsgrid)
    
    print('Input i and j start position')
    i = int(input())
    j = int(input())
    
    foundWords = set()
    word = ""
    visited = {}
    for x in range(0, n):
        for y in range(0, m):
            visited[(x, y)] = 0
    find_words_from_grid(grid,i,j,n,m,word,dictionary,foundWords,visited)
    print(foundWords)
