def single_number(nums: list) -> int:
    re = nums[0]
    for i in range(1, len(nums)):
        re ^= nums[i]
    return re