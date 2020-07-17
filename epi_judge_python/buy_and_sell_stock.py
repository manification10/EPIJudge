from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    if len(prices) <= 1:
        return 0
    profit = 0
    minSoFar = prices[0]
    for i in range(1,len(prices)):
        price = prices[i]
        minSoFar = min(minSoFar, prices[i])
        profit = max(profit, prices[i]-minSoFar)
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
