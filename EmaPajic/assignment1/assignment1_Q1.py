#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: EmaPajic
"""

import sys

""" Checking if str1 and str2 strings are anagrams, isCaseSensitive tells us if we should check case sensitive anagrams or not:
    First, we are transforming strings to only lowercase if strings should be case insensitve
    For each character in the first string, we are counting the number of appearances of each character and checking if the ofther string has the same number
"""
def are_anagrams(str1,str2,isCaseSensitive):
    
    # array for ASCII characters
    letters = [0]*257
    
    # count characters in str1, ignore upper if case insensitive     
    for i in range(0, len(str1)):
        if str1[i].isupper() and isCaseSensitive == 0 :
            letters[ord(str1[i])-ord('A')+ord('a')] += 1
        elif str1[i].isupper() and isCaseSensitive == 1 :
            letters[ord(str1[i])-ord('a')] += 1
        else:
            letters[ord(str1[i])] += 1
            
    # count characters in str2, ignore upper if case insensitive   
    for i in range(0, len(str2)):
        if str2[i].isupper() and isCaseSensitive == 0 :
            letters[ord(str2[i])-ord('A')+ord('a')] -= 1
        elif str2[i].isupper() and isCaseSensitive == 1 :
            letters[ord(str1[i])-ord('a')] -= 1
        else:
            letters[ord(str2[i])] -= 1
        
    # check if same
    for i in range(0,256):
        if letters[i] != 0:
            return False
 
    return True

""" Checking if 2 sentences are anagrams:
    Firs, we get the array of words from sentences by splitting them
    We put sorted words from first sentence in dictionary and then check for sorted words from second sentence if they are in dictionary
"""
def are_anagrams_of_sentences(str1,str2):
    
    dictionary = {}
    # splitting strings into words
    words1 = str1.split()
    words2 = str2.split()
    
    # putting words from first string into dictionary
    for word in words1:
        sortedWord = ''.join(sorted(word))
        if sortedWord in dictionary:
            dictionary[sortedWord] += 1
        else:
           dictionary[sortedWord] = 1 
    
    # checking for words from second string if they are in dictionary
    for word in words2:
        sortedWord = ''.join(sorted(word))
        if sortedWord in dictionary:
            dictionary[sortedWord] -= 1
        else:
            return 0
    
    # check if all words are mached
    for key in dictionary:
        if dictionary[key] != 0:
            return False
        
    return True

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
