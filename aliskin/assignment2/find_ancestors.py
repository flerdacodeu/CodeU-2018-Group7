import unittest

class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.value = x
        self.left = left
        self.right = right

def build_tree_from_preorder(keys):
    '''
    keys: a list of keys in full preorder (i.e. all none vertices included)
    returns a pointer to the root of binary tree
    '''
    if len(keys) == 0:
        return None
    root = TreeNode(keys[0])
    if (len(keys) == 1):
        return root
    half_len = len(keys) // 2
    left = build_tree_from_preorder(keys[1:(half_len + 1)])
    right = build_tree_from_preorder(keys[half_len + 1:])
    root.left = left
    root.right = right
    return root

def find_ancestors(root, key):
    '''
    Given a tree and a key returns a list of the ancestors of the node with
    value key
    Note: a node is its own ancestor; if there are multiple nodes with the same
    key, the first in preorder traversal will be found
    '''
    if root is None:
        return None
    if (not root.left and not root.right and root.value != key):
        return None
    if (root.value == key):
        return [root.value]
    if (root.left):
        ancestors = find_ancestors(root.left, key)
        if ancestors:
            ancestors.append(root.value)
            return ancestors
    if (root.right):
        ancestors = find_ancestors(root.right, key)
        if ancestors:
            ancestors.append(root.value)
            return ancestors
    return None

class TestAncestors(unittest.TestCase):
    def setUp(self):
        self.empty_tree = build_tree_from_preorder([])
        self.example_tree = build_tree_from_preorder([7, 3, 2, 1, 6, 5, None, None, 4, None, None, None, 8, None, None])
        self.full_tree = build_tree_from_preorder(range(1, 32))

    def test_example(self):
        self.assertEqual(find_ancestors(self.example_tree, 6), [6, 2, 3, 7], 'Incorrect ancestors')
        self.assertIsNone(find_ancestors(self.example_tree, 10))

    def test_empty(self):
        self.assertIsNone(find_ancestors(self.empty_tree, 1))

    def test_full(self):
        self.assertEqual(find_ancestors(self.full_tree, 16), [16, 14, 10, 2,
            1])
        self.assertIsNone(find_ancestors(self.full_tree, 32))

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestAncestors('test_example'))
    suite.addTest(TestAncestors('test_empty'))
    suite.addTest(TestAncestors('test_full'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__ == '__main__':
    main()

