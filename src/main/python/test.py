def solve(heights, weights):
    le = len(heights)
    nums = list(range(0, le))
    nums.sort(key=lambda i: [heights[i], weights[i]])
    return list(map(lambda x: x + 1, nums))


print(solve([100, 100, 120, 130], [40, 30, 60, 50]))
