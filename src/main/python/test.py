from sortedcontainers import SortedList


class StockPrice:
    def __init__(self):
        # minimum, maximum使用有序队列
        # current使用Hash
        self.sorted_prices = SortedList()
        self.prices_map = {}
        self.current_ts = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.prices_map:
            self.sorted_prices.remove(self.prices_map[timestamp])
        self.sorted_prices.add(price)
        self.prices_map[timestamp] = price
        self.current_ts = max(self.current_ts, timestamp)

    def current(self) -> int:
        return self.prices_map[self.current_ts]

    def maximum(self) -> int:
        return self.sorted_prices[-1]

    def minimum(self) -> int:
        return self.sorted_prices[0]


stock_price = StockPrice()
stock_price.update(1, 10)
stock_price.update(2, 5)
assert stock_price.current() == 5
assert stock_price.maximum() == 10
assert stock_price.minimum() == 5
stock_price.update(1, 3)
assert stock_price.maximum() == 5
stock_price.update(4, 2)
assert stock_price.minimum() == 2

