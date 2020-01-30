def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    flag = 1 if x > 0 else -1
    re = 0
    abs_x = abs(x)
    while abs_x > 0:
        quo, rem = divmod(abs_x, 10)
        re = re * 10 + rem
        abs_x = quo
    result = flag * re
    return result if -2 ** 31 < result < 2 ** 31 - 1 else 0


print((1 << 31) - 1)
print(reverse(1534236469))
# 1534236469
# 2147483647
