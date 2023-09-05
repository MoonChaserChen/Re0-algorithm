# 只出现一次的数字 II
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。

```
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
    输入: [2,2,3,2]
    输出: 3
    
示例 2:
    输入: [0,1,0,1,0,1,99]
    输出: 99
```

来源：[LeetCode](https://leetcode-cn.com/problems/single-number-ii)

## 模拟三进制
[传送门](https://leetcode-cn.com/problems/single-number-ii/solution/single-number-ii-mo-ni-san-jin-zhi-fa-by-jin407891/)
```python
def single_number(nums: [int]) -> int:
    ones, twos = 0, 0
    for num in nums:
        ones ^= num & ~twos
        twos ^= num & ~ones
    return ones
```