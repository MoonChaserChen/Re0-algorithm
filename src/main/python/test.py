class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7
        dp = [1] * target if k >= target else [1] * k + [0] * (target - k)
        for i in range(1, n):
            for j in range(target - 1, -1, -1):
                if j >= i:
                    dp[j] = sum(dp[max(0, j - k):j]) % mod
                else:
                    dp[j] = 0
        return dp[-1]

s = Solution()
assert s.numRollsToTarget(1, 6, 3) == 1
assert s.numRollsToTarget(2, 6, 7) == 6
assert s.numRollsToTarget(30, 30, 500) == 222616187
assert s.numRollsToTarget(2, 12, 8) == 7