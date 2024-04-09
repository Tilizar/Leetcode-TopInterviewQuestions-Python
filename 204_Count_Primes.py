import math


def countPrimes(n: int) -> int:
    if n <= 2:
        return 0
    array = [True] * n
    array[0] = array[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if not array[i]:
            continue
        for j in range(i ** 2, n, i):
            array[j] = False

    return array.count(True)


if __name__ == '__main__':
    assert 4 == countPrimes(10)
    assert 0 == countPrimes(0)
    assert 0 == countPrimes(1)
