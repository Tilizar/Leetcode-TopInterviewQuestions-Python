from typing import List


def maxProfit(prices: List[int]) -> int:
    prev = prices[0]
    profit = 0

    for i in range(1, len(prices)):
        current = prices[i]
        if current > prev:
            profit += current - prev
        prev = current

    return profit


if __name__ == '__main__':
    assert 7 == maxProfit([7, 1, 5, 3, 6, 4])
    assert 4 == maxProfit([1, 2, 3, 4, 5])
    assert 0 == maxProfit([7, 6, 4, 3, 1])
