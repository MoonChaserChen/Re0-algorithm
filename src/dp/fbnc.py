import timeit


# 递归
def fbnc(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fbnc(n - 1) + fbnc(n - 2)


# 自顶向下
def fbnc_dp0(n):
    dp = [0] * (n + 1)

    def fbnc_dp_arr(i, arr):
        if arr[i]:
            return arr[i]
        if i == 0 or i == 1:
            return i
        arr[i] = fbnc_dp_arr(i - 1, arr) + fbnc_dp_arr(i - 2, arr)
        return arr[i]

    return fbnc_dp_arr(n, dp)


# 自底向上
def fbnc_dp1(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print("fbnc time take:", timeit.timeit("fbnc(15)", setup="from __main__ import fbnc", number=1000))
print("fbnc_dp0 time take:", timeit.timeit("fbnc_dp0(15)", setup="from __main__ import fbnc_dp0", number=1000))
print("fbnc_dp1 time take:", timeit.timeit("fbnc_dp1(15)", setup="from __main__ import fbnc_dp1", number=1000))
