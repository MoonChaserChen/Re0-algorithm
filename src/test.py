def hamming_weight(n: int) -> int:
    re = 0
    while n > 0:
        re += n & 1
        n >>= 1
    return re