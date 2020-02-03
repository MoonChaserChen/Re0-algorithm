def is_valid(s):
    """
    :type s: str
    :rtype: bool
    """
    if s is None: return False
    if s == '': return True
    dic = {"(": ")", "{": "}", "[": "]"}
    stack = []
    for x in s:
        if x in dic:
            stack.append(x)
        else:
            if stack and dic[stack[-1]] == x:
                stack.pop()
            else:
                return False
    return len(stack) == 0