# 求众数 III
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。

```
示例 1:

输入: [3,2,3]
输出: [3]
示例 2:

输入: [1,1,1,3,3,2,2,2]
输出: [1,2]
```

来源：[LeetCode](https://leetcode-cn.com/problems/majority-element-ii)

## 解答
移除三个不一样的数，不影响结果
```python
def majority_element(nums: [int]) -> int:
    m1, s1 = None, 0
    m2, s2 = None, 0
    for x in nums:
        # 新一轮候选
        if s1 == 0 and m2 != x: m1 = x
        elif s2 == 0 and m1 != x: m2 = x
        # 对候选进行计数
        if x == m1: s1 += 1
        elif x == m2: s2 += 1
        # 核心：移除三个不一样的数，不影响结果
        else: s1, s2 = s1 - 1, s2 - 1
    c1, c2 = 0, 0
    for x in nums:
        if x == m1: c1 += 1
        elif x == m2: c2 += 1
    re = []
    if c1 > len(nums) // 3: re.append(m1)
    if c2 > len(nums) // 3: re.append(m2)
    return re
```