def last_remaining(n: int, m: int) -> int:
    re = 0
    for i in range(2, n + 1):
        re = (re + m) % i
    return re