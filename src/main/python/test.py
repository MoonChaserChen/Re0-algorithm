def split_num(num: int) -> int:
    num_str = "".join(sorted(str(num)))
    num1, num2 = int(num_str[::2]), int(num_str[1::2])
    return num1 + num2

assert split_num(4325) == 59
assert split_num(687) == 75
