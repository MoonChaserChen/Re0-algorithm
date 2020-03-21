def rob(nums: [int]) -> int:
    t1, t2 = 0, 0
    for i in range(len(nums)):
        t1, t2 = t2, max(t1 + nums[i], t2)
    return t2
