s0 = "BBC ABCDAB ABCDABCDABDE"
p0 = "ABCDABD"


def KMP(s, p):
    p_len = len(p)
    next = [0] * p_len

