def int2roman(n):
    """
    :type s: int
    :rtype: str
    """
    d_r_m = {"I":1, "V":5, "X": 10, "L":50, "C":100, "D": 500, "M":1000}
    result = ''
    thousand, thousand_left = divmod(n, 1000)
    for i in range(thousand):
        result += 'M'
    hundred, hundred_left = divmod(thousand_left, 100)
    if hundred > 5:
        pass

print(int2roman(3))
print(int2roman(4))
print(int2roman(9))
print(int2roman(58))
print(int2roman(1994))
