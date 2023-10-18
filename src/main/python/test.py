import heapq
import math
from typing import List


class MaxHeap:
    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-x for x in data]
            heapq.heapify(self.data)

    def push(self, item):
        heapq.heappush(self.data, -item)

    def pop(self):
        return -heapq.heappop(self.data)


def max_kelements(nums: List[int], k: int) -> int:
    q = [-x for x in nums]
    heapq.heapify(q)

    ans = 0
    for _ in range(k):
        x = heapq.heappop(q)
        ans += -x
        heapq.heappush(q, -((-x + 2) // 3))
    return ans


assert max_kelements([10, 10, 10, 10, 10], 5) == 50
assert max_kelements([1, 10, 3, 3, 3], 3) == 17
