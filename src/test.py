class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def max_depth(root: TreeNode) -> int:
    if root is None: return 0
    return max(max_depth(root.left), max_depth(root.right)) + 1