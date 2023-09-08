def get_shortest_step(nums):
    le = len(nums)
    steps = []
    for i in range(1, le // 2):
        step = 1
        while i < le - 1:
            i += nums[i]
            step += 1
        if i == le - 1:
            steps.append(step)
    return -1 if len(steps) == 0 else min(steps)


print(get_shortest_step([7, 5, 9, 4, 2, 6, 8, 3, 5, 4, 3, 9]))
print(get_shortest_step([1, 2, 3, 7, 1, 5, 9, 3, 2, 1]))
