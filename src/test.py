def is_happy(n: int) -> bool:
    slow, fast = hn(n), hn(hn(n))
    while slow != fast:
        slow, fast = hn(slow), hn(hn(fast))
    return slow == 1

def hn(n: int) -> int:
    s = 0
    while n:
        r = n % 10
        s += r * r
        n //= 10
    return s