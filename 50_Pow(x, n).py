def myPow(x: float, n: int) -> float:
    def internalPow(x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n % 2 == 0:
            return internalPow(x * x, n // 2)
        else:
            return x * internalPow(x, n - 1)

    if n > 0:
        return internalPow(x, n)
    else:
        return 1 / internalPow(x, -n)


if __name__ == '__main__':
    assert 1024 == myPow(2, 10)
    assert 9.261 == round(myPow(2.1, 3), 4)
    assert 0.25 == myPow(2, -2)
