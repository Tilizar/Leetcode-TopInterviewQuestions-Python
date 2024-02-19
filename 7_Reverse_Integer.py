import math


def reverse(x: int) -> int:
    output = 0

    int_min_value = math.pow(-2, 31)
    int_max_value = math.pow(2, 31) - 1

    min_except_last = int_min_value // 10
    max_except_last = int_max_value // 10

    last_min = int_min_value % 10
    last_max = int_max_value % 10

    while x:
        digit = int(math.fmod(x, 10))
        if output < min_except_last or (output == min_except_last and digit <= last_min):
            return 0
        if output > max_except_last or (output == max_except_last and digit >= last_max):
            return 0

        output = output * 10 + digit
        x = int(x / 10)

    return output


if __name__ == '__main__':
    assert 321 == reverse(123)
    assert -321 == reverse(-123)
    assert 21 == reverse(120)
