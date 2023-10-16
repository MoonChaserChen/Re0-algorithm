from typing import List


def single_number(nums: List[int]) -> int:
    bit_arr = [0] * 32
    for num in nums:
        for i in range(32):
            bit_arr[i] += num & 1
            num >>= 1
    result = 0
    for i in range(32):
        result <<= 1
        result |= bit_arr[31 - i] % 3
    return result if bit_arr[31] % 3 == 0 else ~(result ^ 0xffffffff)

