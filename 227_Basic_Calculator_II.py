def calculate(s: str) -> int:
    stack = []
    pointer = 0
    current_digit = 0
    current_sign = '+'
    signs = ['+', '-', '*', '/']

    while pointer < len(s):
        if s[pointer].isdigit():
            current_digit = current_digit * 10 + int(s[pointer])
        if s[pointer] in signs or pointer == len(s) - 1:
            if current_sign == '+':
                stack.append(current_digit)
            if current_sign == '-':
                stack.append(-current_digit)
            if current_sign == '*':
                stack.append(stack.pop() * current_digit)
            if current_sign == '/':
                stack.append(int(stack.pop() / current_digit))
            current_sign = s[pointer]
            current_digit = 0
        pointer += 1

    output = 0
    for digit in stack:
        output += digit
    return output


if __name__ == '__main__':
    assert 7 == calculate('3+2*2')
    assert 1 == calculate(' 3/2 ')
    assert 5 == calculate(' 3+5 / 2 ')
