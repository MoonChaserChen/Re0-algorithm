def max_profit(prices: list) -> int:
    min_val = None
    profit = 0
    for x in prices:
        if min_val is None or x < min_val:
            min_val = x
        else:
            profit = max(profit, x - min_val)
    return profit