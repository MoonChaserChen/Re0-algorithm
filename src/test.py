def rotate(nums: [int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    le = len(nums)
    start, count = 0, 0
    while start != le and count != le:
        curr = start
        tmp = nums[curr]
        while True:
            ne = (curr + k) % le
            tmp, nums[ne] = nums[ne], tmp
            curr = ne
            count += 1
            if curr == start: break
        start += 1


num = [1,2,3,4,5,6,7]
k = 3
rotate(num, k)
print(num)