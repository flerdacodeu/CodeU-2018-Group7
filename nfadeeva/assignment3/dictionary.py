import collections
from typing import List


class Node:
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.is_word = False


class Dictionary:
    """
    Dictionary class that looks like a trie
    """

    def __init__(self, data: List[str]):
        """
        :param data: list of words
        :type data: List[str]
        """

        self.root = Node()
        for word in data:
            self.add(word)

    def add(self, word):
        """
        Add the word into the dictionary
        """

        node = self.root
        for c in word:
            if c not in node.children:
                # add new character
                node.children[c] = Node()
            node = node.children[c]
        node.is_word = True

    def is_prefix(self, prefix):
        """
        :return: True if the prefix in the dictionary, else - False
        """

        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

    def is_word(self, word):
        """
        :return: True if the word in the dictionary, else - False
        """

        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_word
