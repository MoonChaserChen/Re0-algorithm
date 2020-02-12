arr0 = [
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]

def get_row(row_index: int) -> list:
    arr = [1] * (row_index + 1)
    if row_index < 2: return arr
    for i in range(2, row_index + 1):
        for j in range(i - 1, 0, -1):
            arr[j] += arr[j - 1]
    return arr

print(get_row(0))
print(get_row(1))
print(get_row(2))
print(get_row(3))
print(get_row(4))
print(get_row(5))
print(get_row(6))
print(get_row(7))
print(get_row(8))
print(get_row(9))
print(get_row(10))

