class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_balanced( root: TreeNode) -> bool:
    def is_balanced_helper(top: TreeNode) -> (bool, int):
        if not top: return True, 0
        left_balance, left_height = is_balanced_helper(top.left)
        right_balance, right_height = is_balanced_helper(top.right)
        if left_balance and right_balance and abs(left_height - right_height) < 2:
            return True, max(left_height, right_height) + 1
        return False, -1
    return is_balanced_helper(root)[0]