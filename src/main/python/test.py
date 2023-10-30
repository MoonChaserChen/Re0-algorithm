from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # 答案在 [lo, hi] 中
        lo, hi = 0, len(citations)
        while lo < hi:
            # lo 可能不增加，因此mid偏向于hi
            mid = (lo + hi + 1) // 2
            if citations[-mid] >= mid:
                # lo 可能也是答案
                lo = mid
            else:
                hi = mid - 1
        return lo


print(Solution().hIndex([0, 1, 3, 5, 6]))
print(Solution().hIndex([1, 2, 100]))
