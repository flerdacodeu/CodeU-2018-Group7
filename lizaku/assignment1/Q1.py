import string
import re

def anagrams_words(w1, w2, case_insensitive=True):
    if case_insensitive:
        w1 = w1.lower()
        w2 = w2.lower()
    if len(w1) != len(w2):
        return False
    letters1 = list(w1)
    letters2 = list(w2)
    while letters1 != [] or letters2 != []:
        for letter in letters1:
            if letter in letters2:
                letters1.remove(letter)
                letters2.remove(letter)
            else:
                return False
    return True


# In this question I ignore the punctuation marks. That is, they are not counted as a part of the word. 
# I split the words by punctuation marks and whitespace characters and filter them out.

def anagrams_sentences(s1, s2, case_insensitive=True):
    if case_insensitive:
        s1 = s1.lower()
        s2 = s2.lower()
    words1 = [x for x in re.split('[' + string.punctuation + '\\s]', s1) if x]
    words2 = [x for x in re.split('[' + string.punctuation + '\\s]', s2) if x]
    if len(words1) != len(words2):
        return False
    while words1 != [] or words2 != []:
        for w1 in words1:
            found = False
            for w2 in words2:
                if anagrams_words(w1, w2):
                    found = True
                    words1.remove(w1)
                    words2.remove(w2)
                    break
            if not found:        
                return False
    return True
                
    
    
print(anagrams_words('apple', 'appel', case_insensitive=False))
print(anagrams_sentences('Good, morning! world', 'doog world mornign!'))
