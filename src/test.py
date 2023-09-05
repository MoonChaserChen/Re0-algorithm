def solve(int_list):
    sum_left, sum_right = 0, 0
    for i, x in enumerate(int_list):
        if i == 0:
            sum_left, sum_right = int_list[i], sum(int_list)
        else:
            sum_left += int_list[i]
            sum_right -= int_list[i - 1]
        if sum_left == sum_right:
            return i
    return -1


print(solve(list(map(int, "11".split(',')))))
