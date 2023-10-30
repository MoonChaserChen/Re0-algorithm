def permute(nums):
    n = len(nums)
    res = []

    def back_tracing(curr_idx):
        if curr_idx == n - 1:
            res.append(nums[:])
            return
        chosen_num = []
        # 同层去重
        for i in range(curr_idx, n):
            if nums[i] in chosen_num:
                continue
            chosen_num.append(nums[i])
            nums[curr_idx], nums[i] = nums[i], nums[curr_idx]
            back_tracing(curr_idx + 1)
            nums[curr_idx], nums[i] = nums[i], nums[curr_idx]

    back_tracing(0)
    return res


print(permute([1, 1, 3]))
