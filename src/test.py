def max_product(nums: [int]) -> int:
    max_re = max_step = min_step = None
    for num in nums:
        if max_re is None:
            max_re = max_step = min_step = num
        else:
            candidate = [max_step * num, min_step * num, num]
            max_step = max(candidate)
            min_step = min(candidate)
            if max_step > max_re:
                max_re = max_step
    return max_re
