def convert2title(n: int) -> str:
    ar = ""
    while n > 0:
        c = n % 26
        if c == 0:
            c = 26
            n -= 1
        ar += chr(ord('A') - 1 + c)
        n //= 26
    return ar[::-1]