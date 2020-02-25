def trailing_zeroes(n: int) -> int:
    c = 0
    while n > 0:
        n //= 5
        c += n
    return c