from typing import List


class Solution:
    """
    至少发表了 h 篇论文，并且每篇论文 至少 被引用 h 次
    """
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        # counter[i] 表示被引用了i次的论文数
        counter = [0] * (n + 1)
        for x in citations:
            if x > n:
                counter[n] += 1
            else:
                counter[x] += 1
        tot = 0
        # 从大到小不断check
        for i in range(n, -1, -1):
            # tot 表示至少被引用了i次的论文数
            tot += counter[i]
            # check： 发表了 i 篇论文，并且每篇论文 至少 被引用 i 次
            if tot >= i:
                return i


s = Solution()
assert s.hIndex([3, 0, 6, 1, 5]) == 3
assert s.hIndex([1, 3, 1]) == 1
assert s.hIndex([0, 0, 0]) == 0
assert s.hIndex([8, 7, 6, 5, 3]) == 4
