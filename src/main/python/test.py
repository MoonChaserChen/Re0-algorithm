def permute(nums):
    n = len(nums)
    res = []

    def back_tracing(choose_idx):
        if choose_idx == n - 1:
            res.append(nums[:])
        else:
            for i in range(choose_idx, n):
                nums[choose_idx], nums[i] = nums[i], nums[choose_idx]
                back_tracing(choose_idx + 1)
                nums[choose_idx], nums[i] = nums[i], nums[choose_idx]

    back_tracing(0)
    return res


print(permute([1, 2, 3]))
