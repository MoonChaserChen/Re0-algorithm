def reverse_bits(n: int) -> int:
    res = 0
    c = 31
    while n != 0:
        res |= (n & 1) << c
        c -= 1
        n >>= 1
    return res