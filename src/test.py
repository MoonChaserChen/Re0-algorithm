def get_next(p):
    p_len = len(p)
    p_next = [0] * p_len
    previous_len = 0  # length of the previous longest prefix suffix
    i = 1
    while i < p_len:
        if p[i] == p[previous_len]:
            previous_len += 1
            p_next[i] = previous_len
            i += 1
        else:
            if previous_len != 0:
                previous_len = p_next[previous_len - 1]
            else:
                p_next[i] = 0
                i += 1
    return p_next


txt = "BBC ABCDAB ABCDABCDABDE"
pat = "ABCDABD"
print(get_next(pat))


# ABCDABD
# 0000120

# ABCDEABCDF
# 0000012340

# next[i] =
# next[i - 1] == 0 ? (p[i] == p[0] ? 1 : 0) : (p[i] == p[r] ? next[i - 1] + 1 : 0)
# 当连续匹配上时（next[i] > 0），使用idx_r记录最长的index

# 最长匹配前后缀的特点是：next[i] 与 next[i-1]相关，递增或置0
# 递增条件：p[i] == p[idx_r]，其中idx_r表示：当连续匹配上时（next[i] > 0），使用idx_r记录最长的匹配前缀（当未能匹配上时，idx_r置0）

def get_next0(p):
    p_len = len(p)
    p_next = [0] * p_len
    p_next[0] = 0
    idx_r = 0
    for i in range(1, p_len):
        if p_next[i - 1] == 0:
            p_next[i] = 1 if p[0] == p[i] else 0
        else:
            p_next[i] = p_next[i - 1] + 1 if p[i] == p[idx_r] else 0
        idx_r = idx_r + 1 if p_next[i] != 0 else 0
    return p_next


def get_next1(p):
    p_len = len(p)
    p_next = [0] * p_len
    p_next[0] = 0
    idx_r = 0
    for i in range(1, p_len):
        p_next[i] = p_next[i - 1] + 1 if p[i] == p[idx_r] else 0
        idx_r = idx_r + 1 if p_next[i] != 0 else 0
    return p_next


print(get_next1("ABCDABDABC"))
print(get_next1("ABCDEABCDF"))
print(get_next1("ABDAEFGHIABDA"))
