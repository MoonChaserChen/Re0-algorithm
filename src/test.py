class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def level_order_bottom(root: TreeNode) -> list:
    if not root: return []
    stack = [(root, 0)]
    re = []
    while stack:
        node, depth = stack.pop()
        if len(re) < depth + 1:
            re.append([])
        re[depth].append(node.val)
        if node.right: stack.append((node.right, depth + 1))
        if node.left: stack.append((node.left, depth + 1))
    return re[::-1]
