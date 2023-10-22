from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        # pre[i]表示左侧最小值
        pre, suf = nums.copy(), nums.copy()
        for i in range(1, n):
            pre[i] = min(pre[i], pre[i - 1])
        for i in reversed(range(n - 1)):
            suf[i] = min(suf[i], suf[i + 1])
        ans = -1
        for i in range(1, n - 1):
            if pre[i - 1] < nums[i] and suf[i + 1] < nums[i]:
                pans = nums[i] + pre[i - 1] + suf[i + 1]
                if ans == -1 or ans > pans:
                    ans = pans
        return ans