def next_permutation(nums):
    n = len(nums)
    # 倒序找到第一个降序的值下标s_i
    s_i = n - 2
    while s_i >= 0 and nums[s_i] >= nums[s_i + 1]:
        s_i -= 1
    # 倒序找到第一个比nums[s_i]大的数并与nums[s_i]交换
    if s_i >= 0:
        b_i = n - 1
        while nums[b_i] <= nums[s_i]:
            b_i -= 1
        nums[b_i], nums[s_i] = nums[s_i], nums[b_i]
    # 将s_i后面的数逆序排列
    lo, hi = s_i + 1, n - 1
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        hi -= 1
        lo += 1


arr = [1, 2, 3]
next_permutation(arr)
assert arr == [1, 3, 2]

arr = [1, 1, 5]
next_permutation(arr)
assert arr == [1, 5, 1]

arr = [3, 2, 1]
next_permutation(arr)
assert arr == [1, 2, 3]
