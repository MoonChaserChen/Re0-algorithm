import timeit


class MaxSumSubSequence:
    def __init__(self, arr):
        self.arr = arr

    # 暴力解法
    def bruce(self):
        le = len(self.arr)
        max_result = None
        for i in range(le):
            for j in range(i + 1):
                max_result = max(max_result, sum(self.arr[j:i + 1])) if max_result else sum(self.arr[j:i + 1])
        return max_result

    # 递归
    def ite(self):
        # 以index为ix结尾的连续子序列最大和
        def ite_step(ix):
            if ix == 0:
                return self.arr[ix]
            return self.arr[ix] if ite_step(ix - 1) <= 0 else self.arr[ix] + ite_step(ix - 1)

        le = len(self.arr)
        return max(ite_step(i) for i in range(le))

    # 自顶向下动态规则
    def dp(self):
        le = len(self.arr)
        dp = [None] * le

        # 以index为ix结尾的连续子序列最大和
        def ite_step(ix):
            if ix == 0:
                return self.arr[0]
            if dp[ix]:
                return dp[ix]
            dp[ix] = self.arr[ix] if ite_step(ix - 1) <= 0 else self.arr[ix] + ite_step(ix - 1)
            return dp[ix]

        return max(ite_step(i) for i in range(le))

    # 自底向上动态规则
    def dp1(self):
        le = len(self.arr)
        dp = [None] * le
        dp[0] = self.arr[0]
        # dp[i]表示以index为i结尾的连续子序列最大和
        for i in range(1, le):
            dp[i] = dp[i - 1] + self.arr[i] if dp[i - 1] > 0 else self.arr[i]
        return max(dp)

    # 自底向上省空间
    def dp2(self):
        le = len(self.arr)
        # max_sum 表示连续子序列最大和
        # max_step表示以index为i结尾的连续子序列最大和
        # 将上面dp1()方法的的dp[]用max_sum和max_step来表示
        max_sum = max_step = self.arr[0]
        for i in range(1, le):
            max_step = self.arr[i] if max_step <= 0 else max_step + self.arr[i]
            max_sum = max(max_sum, max_step)
        return max_sum


data = [-14, -19, 8, 7, 7, 7, 3, 11, 8, -9, -6, -1]
mss = MaxSumSubSequence(data)
print("bruce result:", mss.bruce(), ", take time:", timeit.timeit("MaxSumSubSequence([-14, -19, 8, 7, 7, 7, 3, 11, 8, -9, -6, -1]).bruce()", setup="from __main__ import MaxSumSubSequence", number=10000))
print("ite result:", mss.ite(), ", take time:", timeit.timeit("MaxSumSubSequence([-14, -19, 8, 7, 7, 7, 3, 11, 8, -9, -6, -1]).ite()", setup="from __main__ import MaxSumSubSequence", number=10000))
print("dp from top result:", mss.dp(), ", take time:", timeit.timeit("MaxSumSubSequence([-14, -19, 8, 7, 7, 7, 3, 11, 8, -9, -6, -1]).dp()", setup="from __main__ import MaxSumSubSequence", number=10000))
print("dp from bottom result:", mss.dp1(), ", take time:", timeit.timeit("MaxSumSubSequence([-14, -19, 8, 7, 7, 7, 3, 11, 8, -9, -6, -1]).dp1()", setup="from __main__ import MaxSumSubSequence", number=10000))
print("dp from bottom save space result:", mss.dp2(), ", take time:", timeit.timeit("MaxSumSubSequence([-14, -19, 8, 7, 7, 7, 3, 11, 8, -9, -6, -1]).dp2()", setup="from __main__ import MaxSumSubSequence", number=10000))
