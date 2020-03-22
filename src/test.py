class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rob(root: TreeNode) -> int:
    def rob_internal(node: TreeNode):
        if not node: return 0, 0
        re_left, re_right = rob_internal(node.left), rob_internal(node.right)
        re0 = max(re_left) + max(re_right)
        re1 = node.val + re_left[0] + re_right[0]
        return re0, re1
    return max(rob_internal(root))
