# BigDecimal相加
```python
import copy


class BigDecimal:
    def __init__(self, v_str):
        if v_str is not None:
            arr = list(v_str)
            arr.reverse()
            self.r_a = copy.deepcopy(arr)

    def __str__(self):
        r_arr = copy.deepcopy(self.r_a)
        r_arr.reverse()
        return ''.join(r_arr)

    def add(self, another_bd):
        """
        :type another_bd BigDecimal
        """
        le1 = len(self.r_a)
        le2 = len(another_bd.r_a)
        i, up_in, re = 0, 0, []
        for i in range(max(le1, le2)):
            a1 = int(self.r_a[i]) if i < le1 else 0
            a2 = int(another_bd.r_a[i]) if i < le2 else 0
            s = a1 + a2 + up_in
            if s > 9:
                s -= 10
                up_in = 1
            else:
                up_in = 0
            re.append(str(s))
        if up_in == 1:
            re.append('1')
        result = BigDecimal(None)
        result.r_a = re
        return result


bd1 = BigDecimal("32675766")
bd2 = BigDecimal("347852948")
print(bd1.add(bd2))

```