def longest_common_prefix(strs):
    n = min(map(len, strs))
    result = ""
    for i in range(n):
        c = None
        for x in strs:
            if c is None:
                c = x[i]
            elif c != x[i]:
                return result
        result += c


assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
