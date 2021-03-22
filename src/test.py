def hamming_weight(n: int) -> int:
    n = n - ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    n = (n + (n >> 4)) & 0x0f0f0f0f
    n = n + (n >> 8)
    n = n + (n >> 16)
    return n & 0x3f


def hamming_weight_1(n: int) -> int:
    n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
    n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
    n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
    n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
    n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)
    return n


print(hamming_weight(3), hamming_weight_1(3))
print(hamming_weight(-3), hamming_weight_1(-3))
print(hamming_weight(95), hamming_weight_1(95))