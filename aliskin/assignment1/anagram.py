from collections import defaultdict

def isAnagram(s, t, case_sensitive=True):
    """
    Given two strings s and t returns True if t is anagram of s and False otherwise.
    """
    if len(s) != len(t):
        return False
    if (not case_sensitive):
        s = s.casefold()
        t = t.casefold()
    symbols = defaultdict(int)
    for c in s:
        symbols[c] += 1
    for c in t:
        symbols[c] -= 1
        if symbols[c] < 0:
            return False
    return True
