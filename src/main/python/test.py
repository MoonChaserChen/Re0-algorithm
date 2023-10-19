from collections import Counter
from functools import reduce
from typing import List


def tuple_same_product(nums: List[int]) -> int:
    n = len(nums)
    c = Counter([nums[i] * nums[j] for i in range(n) for j in range(i + 1, n)])
    return reduce(lambda x, y: x + y, [v * (v - 1) * 4 for _, v in c.items()])
