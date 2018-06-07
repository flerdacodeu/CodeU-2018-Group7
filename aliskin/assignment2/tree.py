class TreeNode():
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
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
    root.left.parent = root
    root.right = right
    root.right.parent = root
    return root

