def max_profit(prices):
    f0, f1, f2 = -prices[0], 0, 0
    for x in prices:
        n_f0 = max(f0, f2 - x)
        n_f1 = f0 + x
        n_f2 = max(f1, f2)
        f0, f1, f2 = n_f0, n_f1, n_f2
    return max(f1, f2)


assert max_profit([1, 2, 3, 0, 2]) == 3
assert max_profit([1]) == 0
