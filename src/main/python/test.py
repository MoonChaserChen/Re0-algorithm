from typing import List


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        i, s, res = 0, 0, 0
        for i in range(len(satisfaction)):
            s += satisfaction[i]
            if s < 0:
                return res
            res += s
        return res


print(Solution().maxSatisfaction([-1, -8, 0, 5, -7]))
