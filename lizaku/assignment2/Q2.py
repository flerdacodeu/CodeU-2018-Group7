from Q1 import Node, BinaryTree, create_tree

def find_lca(cur_node, node1, node2):
    result = find_lca_(cur_node, node1, node2)
    if not isinstance(result, int):
        raise KeyError('At least one of the given values is not found in the tree')
    return result


def find_lca_(cur_node, node1, node2):
    # This algorithm is designed as follows: I start with the root and 
    # try to check whether one node is present in the left subtree and other node
    # is present in the right subtree. If this is the case, then the current node
    # is LCA. If the traversal reaches the leaves and the value is not found, the recursion step
    # returns None. If required values are not found in the right subtree,
    # Then LCA should be found in the left subtree, and I start to inspect it.
    # Otherwise, I start to inspect the right subtree.
    if cur_node is None:
        #return None
        raise KeyError('At least one of the given values is not found in the tree')
    if cur_node.value == node1 or cur_node.value == node2: # reached one of the values
        #print(cur_node.value, cur_node.left.value, cur_node.right.value)
        return cur_node
    try:
        left_subtree = find_lca_(cur_node.left, node1, node2)
    except KeyError:
        left_subtree = None
        #return None
    try:
        right_subtree = find_lca_(cur_node.right, node1, node2)
    except KeyError:
        right_subtree = None
        #return None
    if left_subtree is not None and right_subtree is not None: # found the node which has both values in the subtrees -- lca
        return cur_node.value
    elif right_subtree is None and left_subtree is not None:
        return left_subtree
    elif left_subtree is None and right_subtree is not None: 
        return right_subtree 
    else:
        raise KeyError('At least one of the given values is not found in the tree')
        
if __name__ == '__main__':
    data = [7, 3, 2, 1, 6, 5, None, None, 4, None, None, None, 8, None, None]    
    tree = BinaryTree()
    tree.root = create_tree(data)
    #tree.print_tree(tree.root)
    print(find_lca(tree.root, 12, 11))
