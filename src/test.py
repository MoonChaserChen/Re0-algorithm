from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def is_symmetric( root: TreeNode) -> bool:
    if not root: return True
    dq = deque([root.left, root.right])
    while dq:
        le, ri = dq.popleft(), dq.pop()
        if not le and not ri: continue
        elif not le or not ri: return False
        elif le.val != ri.val: return False
        dq.appendleft(le.right)
        dq.appendleft(le.left)
        dq.append(ri.left)
        dq.append(ri.right)
    return True