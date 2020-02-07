def add_binary(s1, s2):
    i, j = len(s1) - 1, len(s2) - 1
    plus = False
    s = ''
    while i >= 0 or j >= 0:
        b1 = i >= 0 and s1[i] == '1'
        b2 = j >= 0 and s2[j] == '1'
        bv = b1 ^ b2 ^ plus
        plus = b1 and b2 or b2 and plus or plus and b1
        i, j = i - 1, j - 1
        s += '1' if bv else '0'
    if plus: s += '1'
    return s[::-1]

print(add_binary("1010", "1011"))
print(add_binary("1010", "11"))