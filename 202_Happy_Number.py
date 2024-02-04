def isHappy(n: int) -> bool:

    def compute_next(number: int) -> int:
        output = 0

        while number:
            digit = number % 10
            output += digit ** 2
            number = number // 10

        return output

    cache = set()

    while n not in cache:
        cache.add(n)
        n = compute_next(n)
        if n == 1:
            return True

    return False


if __name__ == '__main__':
    assert isHappy(19)
    assert not isHappy(2)
