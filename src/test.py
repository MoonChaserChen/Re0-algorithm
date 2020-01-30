def is_palindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or x % 10 == 0 and x != 0:
        return False
    r_x = 0
    while x > r_x:
        r_x = r_x * 10 + x % 10
        x //= 10
    return x == r_x or x == r_x // 10

print(is_palindrome(123))