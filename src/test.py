class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def min_depth(root: TreeNode) -> int:
    if not root: return 0
    current_level_stack = [root]
    next_level_stack = []
    level_i = 1
    while current_level_stack:
        node = current_level_stack.pop()
        if not node.left and not node.right:
            return level_i
        if node.left: next_level_stack.append(node.left)
        if node.right: next_level_stack.append(node.right)
        if not current_level_stack:
            level_i += 1
            current_level_stack, next_level_stack = next_level_stack, []