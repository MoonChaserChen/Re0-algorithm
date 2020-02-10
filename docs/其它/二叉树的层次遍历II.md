# 二叉树的层次遍历
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

```
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]
```

来源：[LeetCode](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii)

## BFS
使用两个队列，一个表示当前层节点，一个表示下层节点
```python
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def level_order_bottom(root: TreeNode) -> list[list[int]]:
    if not root: return []
    curr_level_nodes = deque([root])
    next_level_nodes = deque([])
    re = []
    level_re = []
    while curr_level_nodes:
        cn = curr_level_nodes.popleft()
        level_re.append(cn.val)
        if cn.left: next_level_nodes.append(cn.left)
        if cn.right: next_level_nodes.append(cn.right)
        if not curr_level_nodes:
            curr_level_nodes = next_level_nodes
            next_level_nodes = deque([])
            re.append(level_re)
            level_re = []
    return re[::-1]
```

## DFS
结果二维数组先竖后横：二叉树节点的深度 = 二维数组的一级下标 + 1
```python
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
```