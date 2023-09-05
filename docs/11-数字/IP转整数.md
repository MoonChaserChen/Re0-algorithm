# IP转整数
## 解法
```python
def ip2int(ip):
    res = 0
    ips = ip.split(".")
    res |= int(ips[0]) << 24
    res |= int(ips[1]) << 16
    res |= int(ips[2]) << 8
    res |= int(ips[3])
    return res


def int2ip(int_v):
    arr = []
    for i in range(4):
        arr.append(int_v & 255)
        int_v >>= 8
    arr.reverse()
    return ".".join(map(str, arr))


print(int2ip(ip2int("1.2.5.9")))
```