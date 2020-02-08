arr = [1, 2, 3, 4, 5]
arr.pop() # 复杂度 O(1)
arr.pop(0) # 虽然带有队列的操作，但其复杂度为 O(n)
print(arr) # [2, 3, 4]