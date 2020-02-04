def cal_shift_mat(p):
    dic = {}
    len_p = len(p)
    for i in range(len_p - 1, -1, -1):
        if p[i] not in dic:
            dic[p[i]] = len_p - i
    return dic

def find(s, p):
    if p == "": return 0
    len_s, len_p = len(s), len(p)
    dic = cal_shift_mat(p)
    idx = 0
    while idx + len_p <= len_s:
        if s[idx: idx + len_p] == p:
            return idx
        elif idx + len_p == len_s:
            return -1
        else:
            idx += dic.get(s[idx + len_p], len_p + 1)
    return -1

print(find("abc", "c"))



