import math
from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    cache = [math.inf] * (amount + 1)
    cache[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin < 0:
                continue
            cache[i] = min(cache[i], 1 + cache[i - coin])

    return cache[amount] if cache[amount] != math.inf else -1


if __name__ == '__main__':
    assert 3 == coinChange([1, 2, 5], 11)
    assert -1 == coinChange([2], 3)
    assert 0 == coinChange([1], 0)
