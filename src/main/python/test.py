def solve(num_arr):
    num_arr.sort()
    choose_num = num_arr[:3]
    choose_num.sort(key=str)
    return int("".join(map(str, choose_num)))

assert solve([21, 30, 62, 5, 31]) == 21305
assert solve([5, 21]) == 215