s0 = "BBC ABCDAB ABCDABCDABDE"
p0 = "ABCDABD"


def match(s, p):
    for i in range(len(s)):
        try:
            for j in range(len(p)):
                if s[i + j] != p[j]:
                    raise Exception()
            return i
        except Exception:
            continue
    return -1


print(match(s0, p0))
print(s0[15:15+7])
