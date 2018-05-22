from collections import defaultdict
from collections import Counter

def is_anagram(s, t, case_sensitive=True):
    """
    Given two strings s and t returns True if t is anagram of s and False otherwise.
    """
    if len(s) != len(t):
        return False
    if (not case_sensitive):
        s = s.casefold()
        t = t.casefold()
    counter_s = Counter(s)
    counter_t = Counter(t)
    return counter_s == counter_t
