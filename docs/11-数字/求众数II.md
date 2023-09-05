# 求众数 II
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

```
示例 1:
    输入: [3,2,3]
    输出: [3]
    
示例 2:
    输入: [1,1,1,3,3,2,2,2]
    输出: [1,2]

示例 3:
    输入: [1, 1, 1, 2, 2, 2, 3]
    输出: None
```

## 解答
先根据“摩尔投票法”选出众数候选，再判定此数是否为众数。
```python
def majority_element(nums: [int]) -> int:
    # 求出候选众数
    s, majority = 0, None
    for x in nums:
        if s == 0: majority = x
        if x != majority: s-= 1
        else: s += 1
    # 检验候选众数是否正确
    c = 0
    for x in nums:
        if x == majority: c += 1
    if c > len(nums) // 2: return majority
```