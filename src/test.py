def count_primes(n: int) -> int:
    arr = [True] * n
    for i in range(n):
        if i <= 1:
            arr[i] = False
        elif arr[i]:
            j = i
            while i * j < n:
                arr[i * j] = False
                j += 1
    return sum([1 if x else 0 for x in arr])


print(count_primes(10))
