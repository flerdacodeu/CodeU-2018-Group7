def isAnagram(s, t, case_sensitive=False):
    """
    Given two strings s and t returns True if t is anagram of s and False otherwise.
    """
    if len(s) != len(t):
        return False
    symbols = [0 for i in range(256)]
    if (!case_sensitive):
        s = s.casefold()
        t = t.casefold()
    for c in s:
        symbols[ord(c)] += 1
    for c in t:
        symbols[ord(c)] -= 1
        if symbols[ord(c)] < 0:
            return False
    return True
