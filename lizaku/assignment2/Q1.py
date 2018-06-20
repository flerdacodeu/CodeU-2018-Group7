# In my solution I create classes for Node (for storing the key and the information about children;
# I assume that we do not have pointers to parent) and for Tree. The Tree class is not really
# advanced and just stores the root of the tree. And prints the tree in pre-traversal order for debugging purposes.


class Node():
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree():
    def __init__(self, root=None):
        self.root = root
    
    def print_tree(self, node):  
        # Here I don't print Nones
        if node.value is not None:
            print(node.value)
        if node.left is not None:
            self.print_tree(node.left)
        if node.right is not None:
            self.print_tree(node.right)
        
# In this function I create a tree from pre-order. The pre-order has None where the nodes are missing
# in a full binary tree. I tried to make it a method of class BinaryTree, but it kept breaking.
def create_tree(data):
    if not data:
        return None
    if len(data) == 1:
        return Node(value=data[0])
    root = Node(value=data[0])
    half_data = len(data) // 2
    left_subtree = data[1:half_data + 1]
    right_subtree = data[half_data + 1:]
    root.left = create_tree(left_subtree)
    root.right = create_tree(right_subtree)
    return root
    

def find_ancestors(cur_node, key):
    # The algorithm is designed as follows: starting from the root, we recursively traverse the tree in pre-order.
    # When the given key is found, we start an array with ancestors, and on previous steps of the recursion 
    # the ancestors are collected. If the key is not found, nothing is collected. The key can then be deleted from the 
    # resulting array. If the key is not present in the tree, returns None.
    if cur_node.value == key: #found the value
        return [key]
    if cur_node.value is None: # did not found the value, reaching the leaves
        raise KeyError('The value is not found')
    if cur_node.left is not None:
        try:
            ancestors = find_ancestors(cur_node.left, key)
            if ancestors:
                ancestors.append(cur_node.value) # collecting ancestors if the value is found
                return ancestors
        except KeyError:
            pass
    if cur_node.right is not None:
        try:
            ancestors = find_ancestors(cur_node.right, key) # same for the right subtree
            if ancestors:
                ancestors.append(cur_node.value)
                return ancestors
        except KeyError:
            pass
    # end of traversal
    raise KeyError('The value is not found')


if __name__ == '__main__': 
    data = [7, 3, 2, 1, 6, 5, None, None, 4, None, None, None, 8, None, None]    
    tree = BinaryTree()
    tree.root = create_tree(data)
    #tree.print_tree(tree.root)
    ancestors = find_ancestors(tree.root, 11)
    if ancestors:
        print(ancestors[1:]) # The first element is the key itself
