def insert_sort(arr):
    le = len(arr)
    for i in range(1, le):
        j = i - 1
        temp = arr[i]
        while j > 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp
    return arr


print(insert_sort([1, 5, 3, 6, 4, 8, 2]))
