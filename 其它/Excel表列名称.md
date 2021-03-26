# Excel表列名称
给定一个正整数，返回它在 Excel 表中相对应的列名称。

```
例如，

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
```


来源：[LeetCode](https://leetcode-cn.com/problems/excel-sheet-column-title)

## 本质进制
```python
def convert2title(n: int) -> str:
    ar = ""
    while n > 0:
        c = n % 26
        if c == 0:
            c = 26
            n -= 1
        ar += chr(ord('A') - 1 + c)
        n //= 26
    return ar[::-1]
```