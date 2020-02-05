def say(s):
    i, le = 0, len(s)
    re = ""
    while i < le:
        ct, c = 1, s[i]
        while i != le - 1 and s[i + 1] == c:
            ct += 1
            i += 1
        re += str(ct) + c
        i += 1
    return re

def count_and_say( n):
    """
    :type n: int
    :rtype: str
    """
    re = "1"
    while n > 1:
        re = say(re)
        n -= 1
    return re

print(say("1"))
print(say("11"))
print(say("21"))
print(say("1211"))
print(say("111221"))