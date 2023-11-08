class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        cnt = [0, 0]
        res = 0
        for x in s:
            if x == "1":
                cnt[1] += 1
                res = max(res, min(cnt) * 2)
            elif cnt[1] > 0:
                cnt = [1, 0]
            else:
                cnt[0] += 1
        return res

print(Solution().findTheLongestBalancedSubstring("01000111"))