import math


def myAtoi(s: str) -> int:
    output = 0
    index = 0

    int_min_value = int(math.pow(-2, 31))
    int_max_value = int(math.pow(2, 31) - 1)
    max_except_last = int_max_value // 10
    last_max = int_max_value % 10

    is_started = False
    is_positive = True

    while index < len(s):
        char = s[index]

        if char.isspace():
            if is_started:
                break
            index += 1
            continue

        if char == '+' or char == '-':
            if is_started:
                break
            is_started = True
            is_positive = char == '+'
            index += 1
            continue

        if char.isdigit():
            is_started = True
            digit = int(char)

            if output > max_except_last or (output == max_except_last and digit > last_max):
                return int_max_value if is_positive else int_min_value

            output = output * 10 + digit
            index += 1
            continue

        break

    return output if is_positive else output * -1


if __name__ == '__main__':
    assert 42 == myAtoi('42')
    assert -42 == myAtoi('   -42')
    assert 4193 == myAtoi('4193 with words')
