def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i, n = 0, len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return i

nums0 = [3, 3, 1, 2, 3, 4]
remove_element(nums0, 3)
print(nums0)