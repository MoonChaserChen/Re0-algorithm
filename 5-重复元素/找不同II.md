# 找不同
给定两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。

```
示例:
输入：
    s = "abcd"
    t = "abcde"

输出：
    e

解释：
    'e' 是那个被添加的字母。
```

来源：[LeetCode](https://leetcode-cn.com/problems/find-the-difference)

## 字符转数字相减
```python
def find_the_difference(s: str, t: str) -> str:
    return chr(sum(map(ord, t)) - sum(map(ord, s)))
```

## 字符转数字用异或
```python
def find_the_difference(s: str, t: str) -> str:
    re_n, le = 0, len(t)
    for i in range(le):
        re_n ^= ord(t[i])
        if i < le - 1: re_n ^= ord(s[i])
    return chr(re_n)
```

```python
def find_the_difference(s: str, t: str) -> str:
    tmp = s + t
    res = ord(tmp[0])
    for t in tmp[1:]:
        res ^= ord(t)
    return chr(res)
```

```python
from functools import reduce
import operator

def find_the_difference(s: str, t: str) -> str:
    return chr(reduce(operator.xor, map(ord, s + t)))
```