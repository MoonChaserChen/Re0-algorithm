def max_profit(prices, fee):
    f0, f1 = 0, -prices[0]
    for x in prices:
        f0 = max(f0, f1 + x - fee)
        f1 = max(f1, f0 - x)
    return f0


assert max_profit([1, 3, 2, 8, 4, 9], 2) == 8
assert max_profit([1, 3, 7, 5, 10, 3], 3) == 6
