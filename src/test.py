arr = [1, 2, 3, 4, 5, 2]
s0 = set(arr)
s1 = {2, 3, 9, 5, 8, 10}
s0.discard(7)  # 7不存在不会报错
s0.remove(1)  # 1不存在会报错
s0.add(8)

print(s0.intersection({4}))  # 取交集
print(s0.isdisjoint({20}))  # 是否没有交集

print(s0.difference(s1))  # 差集：s0 - s1
print(s0.difference_update(s1))  # 差集：s0 = s0 - s1

print(s0.issubset(s1))  # s0是否存为s1的子集

print(s0.symmetric_difference(s1))  # 对称差：(s0 - s1) + (s1 - s0)
print(s0.symmetric_difference_update(s1))  # 对称差：s0 = (s0 - s1) + (s1 - s0)

print(s0.union(s1))  # 并集
s0.update(s1)  # s0 = s0 + s1
