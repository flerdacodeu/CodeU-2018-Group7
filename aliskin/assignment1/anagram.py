from collections import defaultdict
from collections import Counter
import string

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

def main():
    """
    Some simple examples to test the function is_anagram
    """
    test_examples = [('', '', True), 
            ('a', 'A', False),
            ('a', 'aa', False),
            ('apple', 'lappe', True),
            (string.ascii_lowercase, string.ascii_lowercase, True),
            (string.ascii_lowercase, string.ascii_uppercase, False)]
    for s, t, answer in test_examples:
        assert (is_anagram(s, t) == answer), 'Incorrect answer for {} and {}, should be {}'.format(s, t, answer)
    """
    Check case insensitive
    """
    test_examples = [('', '', True),
            ('a', 'A', True),
            ('ABC', 'Cabbba', False),
            (string.ascii_lowercase, string.ascii_lowercase, True),
            (string.ascii_lowercase, string.ascii_uppercase, True)]
    for s, t, answer in test_examples:
        assert (is_anagram(s, t, case_sensitive=False) == answer), 'Incorrect answer for {} and {}, should be {}'.format(s, t, answer)

if __name__ == '__main__':
    main()
