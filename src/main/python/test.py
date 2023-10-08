def final_prices(prices):
    stack = []
    for i, price in enumerate(prices):
        while stack and price <= prices[stack[-1]]:
            t = stack.pop()
            # 直接使用原prices变量保存结果
            prices[t] = prices[t] - price
        stack.append(i)
    return prices


assert final_prices([8, 4, 6, 2, 3]) == [4, 2, 4, 2, 3]
assert final_prices([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert final_prices([10, 1, 1, 6]) == [9, 0, 1, 6]
