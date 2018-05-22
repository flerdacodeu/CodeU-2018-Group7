import string
from collections import Counter
import re


def is_anagram(s1, s2, case_sensitive=False, punctuation=string.punctuation):
    """
    Given two strings, determine if one is an anagram of the other.
    Function able to handle anagrams of sentences, where each word
    in the resulting sentence is an anagram of one of the words in
    the original sentence.

    :param punctuation: symbols that will be ignored
    :return if s1 is an anagram of s2
    """
    # replace all punctuations symbols to space
    s1 = re.sub(r"[{}]".format(punctuation)," ", s1)
    s2 = re.sub(r"[{}]".format(punctuation)," ", s2)
    if not case_sensitive:
        s1 = s1.lower()
        s2 = s2.lower()

    # remove all whitespaces
    s1 = re.sub(r"\s+", " ", s1)
    s2 = re.sub(r"\s+", " ", s2)

    # count characters for every word in both sentences
    count_s1 = [Counter(x) for x in s1.strip().split(' ')]
    count_s2 = [Counter(x) for x in s2.strip().split(' ')]

    # delete from the count_s1 every word that is anagram of the word in count_s2
    for word in count_s2:
        if word not in count_s1:
            return False
        else:
            count_s1.remove(word)
    # if all words from the s2 is anagrams of one of the words in s1 return True
    return not count_s1

print(is_anagram('Hello, World!', 'EollH ordlW'))  # True
print(is_anagram('Hello, World!', 'EollH ordlW', case_sensitive=True))  # False
print(is_anagram('Hello, World!', 'EollH ordlW', punctuation="."))  # False
