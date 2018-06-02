import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def find_lca(root, node1, node2):
    """
        Find the lowest common ancestor of two nodes in a binary tree
        :type node1: Node
        :type node2: Node
        :rtype: Node or False
        :return The lowest common ancestor of two nodes in a binary tree
                if one of the Node is not in the given tree return the existed node
                if both of the given nodes aren't in the given tree return False
        """

    if root is None:
        return False

    if root is node1 or root is node2:
        return root

    # find one of the given nodes in left and right subtrees
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)

    # one of the given key in the left subtree
    # and the other in the right => lca = current root
    if left_lca and right_lca:
        return root

    # the lca should be in the left or in the right subtree
    return left_lca if left_lca else right_lca


# run all tests:
# python3 -m unittest assignment2/Assignment_2_Q2.py
class TestFindLCA(unittest.TestCase):

    def test_example(self):
        root = Node(7)
        root.right = Node(4)
        root.right.right = Node(8)
        root.left = Node(3)
        root.left.left = Node(2)
        node1 = root.left.right = Node(5)
        root.left.left.left = Node(1)
        node2 = root.left.left.right = Node(6)
        self.assertEqual(find_lca(root, node1, node2).data, 3)

    def test_empty_tree(self):
        root = None
        self.assertFalse(find_lca(root, Node(1), Node(2)))

    def test_missed_both_nodes(self):
        """
        Function should return False when the both of given nodes aren't in the given tree

        """
        root = Node(7)
        root.right = Node(4)
        self.assertFalse(find_lca(root, Node(1), Node(2)))

    def test_missed_one_node(self):
        """
        Function should return the existed node when another given node is missed

        """
        root = Node(7)
        node1 = root.right = Node(4)
        self.assertEqual(find_lca(root, node1, Node(2)), node1)