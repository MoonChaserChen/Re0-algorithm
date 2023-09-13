def climb_stairs(n: int):
    dp = [1, 1, 2]
    for i in range(3, n):
        dp.append(dp[i - 1] + dp[i - 3])
    return dp[n - 1]

print(climb_stairs(4))
print(climb_stairs(5))
print(climb_stairs(6))
print(climb_stairs(50))