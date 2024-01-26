from typing import List


def maxProfit(prices: List[int]) -> int:
    buy_index, sell_index = 0, 1
    profit = 0

    while sell_index < len(prices):
        if prices[buy_index] < prices[sell_index]:
            profit = max(profit, prices[sell_index] - prices[buy_index])
        else:
            buy_index = sell_index
        sell_index += 1
    return profit


if __name__ == '__main__':
    assert 5 == maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == maxProfit([7, 6, 4, 3, 1])
