class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def has_path_sum(root: TreeNode, target: int) -> bool:
    if not root: return False
    stack = [(root, root.val)]
    while stack:
        node, s = stack.pop()
        if not node.left and not node.right and s == target:
            return True
        if node.right: stack.append((node.right, s + node.right.val))
        if node.left: stack.append((node.left, s + node.left.val))
    return False