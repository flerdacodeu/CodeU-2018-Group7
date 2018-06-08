import unittest
from tree import TreeNode, build_tree_from_preorder

def find_distance_to_root(node):
    '''
    Returns a distance between a node and a root of the tree
    '''
    current_node = node
    height = 0
    while current_node:
        current_node = current_node.parent
        height += 1
    return height - 1

def find_lca(first_node, second_node):
    '''
    Given two nodes in a tree returns their lowest common ancestor
    '''
    first_height = find_distance_to_root(first_node)
    second_height = find_distance_to_root(second_node)
    current_first_node = first_node
    current_second_node = second_node
    if first_height > second_height:
        for i in range(first_height - second_height):
            current_first_node = current_first_node.parent
    if second_height > first_height:
        for i in range(second_height - first_height):
            current_second_node = current_second_node.parent
    while (current_first_node != current_second_node):
        current_first_node = current_first_node.parent
        current_second_node = current_second_node.parent
    return current_first_node

class TestLCA(unittest.TestCase):
    def setUp(self):
        self.tree = build_tree_from_preorder(range(1, 16))

    def test(self):
        self.assertEqual(find_lca(self.tree, self.tree.left), self.tree) 
        self.assertEqual(find_lca(self.tree.left, self.tree.right.left.left),
                self.tree)
        self.assertEqual(find_lca(self.tree.left, self.tree.right), self.tree)
        self.assertEqual(find_lca(self.tree.right, self.tree.right.left.left),
                self.tree.right)
        self.assertEqual(find_lca(self.tree.left.left.right,
            self.tree.left.right.left), self.tree.left)

    def test_trivial(self):
        self.assertEqual(find_lca(self.tree.left.left, self.tree.left.left),
                self.tree.left.left)

    def stress_test(self):
        tree = TreeNode(0)
        current_node = tree
        for i in range(100000):
            node = TreeNode(i + 1, current_node)
            current_node.left = node
            current_node = node
        tree.right = TreeNode(31, tree)
        self.assertEqual(find_lca(current_node, tree), tree)
        self.assertEqual(find_lca(current_node, tree.right), tree)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestLCA('test'))
    suite.addTest(TestLCA('test_trivial'))
    suite.addTest(TestLCA('stress_test'))
    return suite

def main():
    runner = unittest.TextTestRunner()
    runner.run(suite())

if __name__ == '__main__':
    main()
