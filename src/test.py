def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    n, ct = len(s), 0
    while n > 0:
        n -= 1
        if s[n] == ' ':
            return ct
        else:
            ct += 1
    return ct

print(lengthOfLastWord("a "))