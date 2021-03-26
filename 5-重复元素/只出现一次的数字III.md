# 只出现一次的数字 III
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。

```
示例 :

输入: [1,2,1,3,2,5]
输出: [3,5]
注意：

结果输出的顺序并不重要，对于上面的例子， [5, 3] 也是正确答案。
你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？
```

来源：[LeetCode](https://leetcode-cn.com/problems/single-number-iii)

## 解答
[传送门](https://leetcode-cn.com/problems/single-number-iii/solution/zhi-chu-xian-yi-ci-de-shu-zi-iii-by-leetcode/)
设这两个数为x,y，则所有数异或得到：bitmask = x^y
bitmask & (-bitmask)保留bitmask最右边的1，这个1要么来自x，要么来自y
```python
def single_number(nums: [int]) -> [int]:
    # difference between two numbers (x and y) which were seen only once
    bitmask = 0
    for num in nums:
        bitmask ^= num

    # rightmost 1-bit diff between x and y
    diff = bitmask & (-bitmask)

    x = 0
    for num in nums:
        # bitmask which will contain only x
        if num & diff:
            x ^= num

    return [x, bitmask^x]
```