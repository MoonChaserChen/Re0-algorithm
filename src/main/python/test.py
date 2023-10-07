import math


class StockSpanner:
    def __init__(self):
        # 元素数量
        self.cnt = 0
        # 单调递减栈，栈中保存(元素值，下标)
        self.stack = [(math.inf, -1)]

    def next(self, val):
        while self.stack[-1][0] < val:
            self.stack.pop()
        result = self.cnt - self.stack[-1][1]
        self.stack.append((val, self.cnt))
        self.cnt += 1
        return result


s1 = StockSpanner()
assert s1.next(100) == 1
assert s1.next(80) == 1
assert s1.next(60) == 1
assert s1.next(70) == 2
assert s1.next(60) == 1
assert s1.next(75) == 4
assert s1.next(85) == 6

s2 = StockSpanner()
assert s2.next(31) == 1
assert s2.next(41) == 2
assert s2.next(48) == 3
assert s2.next(59) == 4
assert s2.next(79) == 5