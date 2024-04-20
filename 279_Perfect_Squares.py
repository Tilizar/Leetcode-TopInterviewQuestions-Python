def numSquares(n: int) -> int:
    cache = list(range(0, n + 1))
    cache[0] = 0

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if i < j * j:
                break
            cache[i] = min(cache[i], cache[i - j * j] + 1)

    return cache[n]


if __name__ == '__main__':
    assert 3 == numSquares(12)
    assert 2 == numSquares(13)
