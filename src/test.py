def check_sub_str(strs: str, check: str):
    i, j = 0, 0
    while j < len(strs):
        if strs[j] == check[i]:
            i += 1
            if i == len(check):
                return True
        j += 1
    return False


print(check_sub_str("abcde", "bdskjfhla"))
print(check_sub_str("abcde", "acf"))


