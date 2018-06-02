import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def find_all_ancestors(root, key, result=None):
        """
        Prints all the ancestors of the given key

        :return list of ancestors of the given key or False if the key is not in the Tree
        """

        if root is None:
            return False

        if result is None:
            result = []

        if root.data == key:
            return True

        # append the current root value to the result if the given key
        # in the right or in the left part of the tree (check it recursively)
        elif find_all_ancestors(root.right, key, result) or\
                find_all_ancestors(root.left, key, result):
            result.append(root.data)
            return result

        # the given key is not in the tree
        return False


# run all tests:
# python3 -m unittest assignment2/Assignment_2_Q1.py
class TestPrintAncestors(unittest.TestCase):

    def test_example(self):
        root = Node(7)
        root.right = Node(4)
        root.right.right = Node(8)
        root.left = Node(3)
        root.left.left = Node(2)
        root.left.right = Node(5)
        root.left.left.left = Node(1)
        root.left.left.right = Node(6)
        self.assertEqual(find_all_ancestors(root, 6), [2, 3, 7])

    def test_empty_tree(self):
        root = None
        self.assertFalse(find_all_ancestors(root, 6))

    def test_missed_key(self):
        """
        Function should return False when the given key is not in the given tree

        """
        root = Node(7)
        root.right = Node(4)
        self.assertFalse(find_all_ancestors(root, 6))
