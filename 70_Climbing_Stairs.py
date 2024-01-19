def climbStairs(n: int) -> int:
    a, b = 1, 1

    for i in range(n - 1):
        a, b = b, a + b

    return b


if __name__ == '__main__':
    assert 2 == climbStairs(2)
    assert 3 == climbStairs(3)
