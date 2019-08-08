import timeit


class Triangle:
    def __init__(self, arr):
        self.arr = arr

    # 递归
    def max_route_sum_ite(self):
        def max_route_sum_line(from_x, from_y):
            if from_x == len(self.arr) - 1:
                return self.arr[from_x][from_y]
            return max(max_route_sum_line(from_x + 1, from_y), max_route_sum_line(from_x + 1, from_y + 1)) + self.arr[from_x][from_y]

        return max_route_sum_line(0, 0)

    # 自顶向下动态规划
    def max_route_sum_dp(self):
        le = len(self.arr)
        dp = [[0] * le for i in range(le)]

        def max_route_sum_line(from_x, from_y):
            if dp[from_x][from_y]:
                return dp[from_x][from_y]
            if from_x == len(self.arr) - 1:
                return self.arr[from_x][from_y]
            dp[from_x][from_y] = max(max_route_sum_line(from_x + 1, from_y), max_route_sum_line(from_x + 1, from_y + 1)) + self.arr[from_x][from_y]
            return dp[from_x][from_y]

        return max_route_sum_line(0, 0)

    # 自底向上动态规划
    def max_route_sum_dp1(self):
        le = len(self.arr)
        dp = [[0] * le for i in range(le)]

        for i in reversed(range(le)):
            for j in range(i + 1):
                if i == le - 1:
                    dp[i][j] = self.arr[i][j]
                else:
                    dp[i][j] = self.arr[i][j] + max(dp[i + 1][j], dp[i + 1][j + 1])
        return dp[0][0]

    # 自底向上动态规划省空间
    def max_route_sum_dp2(self):
        le = len(self.arr)
        for i in reversed(range(le - 1)):
            for j in range(i + 1):
                self.arr[i][j] = self.arr[i][j] + max(self.arr[i + 1][j], self.arr[i + 1][j + 1])
        return self.arr[0][0]


data = [[8],
        [5, 19],
        [13, 4, 16],
        [13, 1, 13, 6],
        [18, 15, 8, 16, 3],
        [11, 11, 9, 11, 14, 13],
        [3, 6, 10, 11, 14, 8, 19],
        [17, 20, 0, 13, 7, 13, 5, 20],
        [12, 12, 4, 9, 8, 8, 13, 14, 15],
        [3, 18, 19, 4, 5, 19, 0, 15, 12, 12]]
triangle = Triangle(data)

print("max route sum iteration result:", triangle.max_route_sum_ite(), end=', ')
print("take time:",
      timeit.timeit("Triangle([[8],\
                    [5, 19],\
                    [13, 4, 16],\
                    [13, 1, 13, 6],\
                    [18, 15, 8, 16, 3],\
                    [11, 11, 9, 11, 14, 13],\
                    [3, 6, 10, 11, 14, 8, 19],\
                    [17, 20, 0, 13, 7, 13, 5, 20],\
                    [12, 12, 4, 9, 8, 8, 13, 14, 15],\
                    [3, 18, 19, 4, 5, 19, 0, 15, 12, 12]]).max_route_sum_ite()",
                    setup="from __main__ import Triangle", number=10000))

print("max route sum dp result:", triangle.max_route_sum_dp(), end=', ')
print("take time:",
      timeit.timeit("Triangle([[8],\
                    [5, 19],\
                    [13, 4, 16],\
                    [13, 1, 13, 6],\
                    [18, 15, 8, 16, 3],\
                    [11, 11, 9, 11, 14, 13],\
                    [3, 6, 10, 11, 14, 8, 19],\
                    [17, 20, 0, 13, 7, 13, 5, 20],\
                    [12, 12, 4, 9, 8, 8, 13, 14, 15],\
                    [3, 18, 19, 4, 5, 19, 0, 15, 12, 12]]).max_route_sum_dp()",
                    setup="from __main__ import Triangle", number=10000))

print("max route sum dp1 result:", triangle.max_route_sum_dp1(), end=', ')
print("take time:",
      timeit.timeit("Triangle([[8],\
                    [5, 19],\
                    [13, 4, 16],\
                    [13, 1, 13, 6],\
                    [18, 15, 8, 16, 3],\
                    [11, 11, 9, 11, 14, 13],\
                    [3, 6, 10, 11, 14, 8, 19],\
                    [17, 20, 0, 13, 7, 13, 5, 20],\
                    [12, 12, 4, 9, 8, 8, 13, 14, 15],\
                    [3, 18, 19, 4, 5, 19, 0, 15, 12, 12]]).max_route_sum_dp1()",
                    setup="from __main__ import Triangle", number=10000))

print("max route sum dp2 result:", triangle.max_route_sum_dp2(), end=', ')
print("take time:",
      timeit.timeit("Triangle([[8],\
                    [5, 19],\
                    [13, 4, 16],\
                    [13, 1, 13, 6],\
                    [18, 15, 8, 16, 3],\
                    [11, 11, 9, 11, 14, 13],\
                    [3, 6, 10, 11, 14, 8, 19],\
                    [17, 20, 0, 13, 7, 13, 5, 20],\
                    [12, 12, 4, 9, 8, 8, 13, 14, 15],\
                    [3, 18, 19, 4, 5, 19, 0, 15, 12, 12]]).max_route_sum_dp2()",
                    setup="from __main__ import Triangle", number=10000))
