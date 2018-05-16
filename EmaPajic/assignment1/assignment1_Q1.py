#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

import sys

def areAnagramsCaseInsensitive(str1,str2):
    
    letters = [0]*27
    for i in range(0, len(str1)):
        if ord(str1[i]) < 97 :
            letters[ord(str1[i])-ord('A')] += 1
        else:
            letters[ord(str1[i])-ord('a')] += 1
    
    for i in range(0, len(str2)):
        if ord(str2[i]) < 97:
            letters[ord(str2[i])-ord('A')] -= 1
        else:
            letters[ord(str2[i])-ord('a')] -= 1
        
    for i in range(0,26):
        if letters[i] != 0:
            return 0
 
    return 1
    
def areAnagramsCaseSensitive(str1,str2):
    
    letters = [0]*27
    CapitalLetters = [0]*27
    for i in range(0, len(str1)):
        if ord(str1[i]) < 97:
            CapitalLetters[ord(str1[i])-ord('A')] += 1
        else:
            letters[ord(str1[i])-ord('a')] += 1
    
    for i in range(0, len(str2)):
        if ord(str2[i]) < 97 :
            CapitalLetters[ord(str2[i])-ord('A')] -= 1
        else:
            letters[ord(str2[i])-ord('a')] -= 1
        
    for i in range(0,26):
        if letters[i] != 0:
            return 0
    for i in range(0,26):
        if CapitalLetters[i] != 0:
            return 0

    return 1

def areAnagramsOfSentences(str1,str2):
    
    dictionary = {}
    words1 = str1.split()
    words2 = str2.split()
    for word in words1:
        sortedWord = ''.join(sorted(word))
        if sortedWord in dictionary:
            dictionary[sortedWord] += 1
        else:
           dictionary[sortedWord] = 1 
    
    for word in words2:
        sortedWord = ''.join(sorted(word))
        if sortedWord in dictionary:
            dictionary[sortedWord] -= 1
        else:
            return 0
        
    for key in dictionary:
        if dictionary[key] != 0:
            return 0
        
    return 1

def main():
    
    sys.stdout.write('Input the first string')
    str1 = input()
    sys.stdout.write('Input the second string')
    str2 = input()
    sys.stdout.write('Choose an option:\n 1. Case insensitive anagrams \n 2. Case sensitive anagrams \n 3. Anagrams of sentences \n')
    option = int(input())
    if option == 1:
        if areAnagramsCaseInsensitive(str1,str2) == 1:
            sys.stdout.write(str1+" and "+str2+" are anagrams")
        else:
            sys.stdout.write(str1+" and "+str2+" are not anagrams")
    elif option == 2:
        if areAnagramsCaseSensitive(str1,str2) == 1:
            sys.stdout.write(str1+" and "+str2+" are anagrams")
        else:
            sys.stdout.write(str1+" and "+str2+" are not anagrams")
    elif option == 3:
        if areAnagramsOfSentences(str1,str2) == 1:
            sys.stdout.write(str1+" and "+str2+" are anagrams")
        else:
            sys.stdout.write(str1+" and "+str2+" are not anagrams")
    else:
        sys.stdout.write("Wrong option")
        
main()
