class Solution:
    def __init__(self, _fixed_len, _arr):
        self.fixed_len = _fixed_len
        self.arr = _arr

    @staticmethod
    def init_from_console():
        fixed_len = int(input())
        return Solution([list(map(int, input().split(","))) for i in range(int(input()))])

    def solve(self):
        n = 0
        for i in range(len(self.arr)):
            for j in range(3):
                self.arr[i][j] += min([x for k, x in enumerate(self.arr[i - 1]) if k != j])
        return min(self.arr[-1])

print([1, 2][3: 4])
