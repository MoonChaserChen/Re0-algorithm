def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs: return ""
    prefix = strs[0]
    for i, v in enumerate(prefix):
        for j in range(1, len(strs)):
            if len(strs[j]) == i or v != strs[j][i]: return prefix[:i]
    return prefix


print(longest_common_prefix(['aaaaa', 'aa']))
