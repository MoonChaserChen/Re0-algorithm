from typing import List


def sum_distance(nums: List[int], s: str, d: int) -> int:
    n = len(nums)
    pos = [nums[i] - d if s[i] == 'L' else nums[i] + d for i in range(n)]
    pos.sort()
    return sum([(pos[i] - pos[i - 1]) * i * (n - i) for i in range(1, n)]) % (10**9 + 7)


assert sum_distance([-2, 0, 2], "RLL", 3) == 8
assert sum_distance([1, 0], "RL", 2) == 5
