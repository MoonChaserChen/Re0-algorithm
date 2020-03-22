def rob(nums: [int]) -> int:
    def my_rob(nums: [int]) -> int:
        t1, t2 = 0, 0
        for num in nums:
            t1, t2 = t2, max(t1 + num, t2)
        return t2
    return max(my_rob(nums[1:]), my_rob(nums[:-1])) if len(nums) != 1 else nums[0]
