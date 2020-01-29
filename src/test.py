def two_sum(nums, target):
    hm = {}
    for i, x in enumerate(nums):
        rem = target - x
        if rem in hm:
            return  hm[rem], i
        hm[x] = i