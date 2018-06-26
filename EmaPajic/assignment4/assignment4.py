#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

def count_islands(rows,columns,tiles):
    """
    I am assuming that we can change tiles (set some values to false).
    If we couldn't do that, we could just make another matrix where we would store flags so that we don't visit same tile twice.
    In this function we are just going through matrix and if we find a part of island we call function find_all_parts_of island to set all parts of that island to false
    """
    numOfIslands = 0
    for i in range(0,rows):
        for j in range(0,columns):
            if tiles[i][j] == True:
                numOfIslands += 1
                find_all_parts_of_island(rows,columns,i,j,tiles)
    return numOfIslands

def valid_index(rows,columns,i,j):
    # check if index is out of range
    if i < 0 or i >= rows or j < 0 or j >= columns:
        return False
    return True
    
def find_all_parts_of_island(rows,columns,i,j,tiles):
    #I am using dfs to find all connected tiles to one we found before we called this function from count_islands
    tiles[i][j] = False
    for move in [-1,1]:
        if valid_index(rows,columns,i+move,j):
            if tiles[i+move][j] == True:
                find_all_parts_of_island(rows,columns,i+move,j,tiles)
        if valid_index(rows,columns,i,j+move):
            if tiles[i][j+move] == True:
                find_all_parts_of_island(rows,columns,i,j+move,tiles)
            
def main():
    #main class if we want to test something that is not in the tests
    rows = int(input())
    columns = int(input())
    tiles = [0] * rows
    for i in range(0,rows):
        tiles[i] = [0] * columns
    for i in range(0,rows):
        for j in range(0,columns):
            tmp = int(input())
            if tmp == 0:
                tiles[i][j] = False
            else:
                tiles[i][j] = True
    num = count_islands(rows,columns,tiles)
    print(num)

    