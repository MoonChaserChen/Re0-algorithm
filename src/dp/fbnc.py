import timeit


# 递归
def fbnc(n):
    return n if n < 2 else fbnc(n - 1) + fbnc(n - 2)


# 自顶向下动态规划
def fbnc_dp0(n):
    dp = [0] * (n + 1)

    def fbnc_dp_step(i):
        if dp[i]:
            return dp[i]
        if i < 2:
            return i
        dp[i] = fbnc_dp_step(i - 1) + fbnc_dp_step(i - 2)
        return dp[i]

    return fbnc_dp_step(n)


# 自底向上动态规划
def fbnc_dp1(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# 自底向上动态规划省空间
def fbnc_dp2(n):
    if n < 2:
        return n
    tmp1, tmp2 = 0, 1
    for i in range(2, n + 1):
        tmp1, tmp2 = tmp2, tmp1 + tmp2
    return tmp2


print("fbnc result:", fbnc(15), ",time take:", timeit.timeit("fbnc(15)", setup="from __main__ import fbnc", number=1000))
print("fbnc_dp0 result:", fbnc_dp0(15), ",time take:", timeit.timeit("fbnc_dp0(15)", setup="from __main__ import fbnc_dp0", number=1000))
print("fbnc_dp1 result:", fbnc_dp1(15), ",time take:", timeit.timeit("fbnc_dp1(15)", setup="from __main__ import fbnc_dp1", number=1000))
print("fbnc_dp2 result:", fbnc_dp2(15), ",time take:", timeit.timeit("fbnc_dp2(15)", setup="from __main__ import fbnc_dp2", number=1000))
