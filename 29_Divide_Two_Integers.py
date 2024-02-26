def divide(dividend: int, divisor: int) -> int:
    if dividend == int(-1 << 31) and divisor == -1:
        return int((1 << 31) - 1)

    is_positive = (dividend >= 0) == (divisor >= 0)
    result = 0
    dividend = abs(dividend)
    divisor = abs(divisor)

    while dividend - divisor >= 0:
        counter = 0
        while dividend - (divisor << 1 << counter) >= 0:
            counter += 1
        result += 1 << counter
        dividend -= divisor << counter

    return result if is_positive else -result


if __name__ == '__main__':
    assert 3 == divide(10, 3)
    assert -2 == divide(7, -3)
