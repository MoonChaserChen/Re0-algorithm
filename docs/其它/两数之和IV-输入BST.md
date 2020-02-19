# 两数之和 IV - 输入 BST
给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

```
案例 1:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

输出: True

案例 2:

输入: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

输出: False
```

来源：[LeetCode](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst)

## BFS+Hash
```python
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_target(root: TreeNode, k: int) -> bool:
    if not root: return False
    dic = {}
    dq = deque([root])
    while dq:
        node = dq.popleft()
        if k - node.val in dic: return True
        dic[node.val] = 1
        if node.left: dq.append(node.left)
        if node.right: dq.append(node.right)
    return False

```
