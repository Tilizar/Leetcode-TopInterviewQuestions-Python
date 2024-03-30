from typing import List


def evalRPN(tokens: List[str]) -> int:
    token = tokens.pop()
    if token.isdigit() or (token.startswith('-') and len(token) > 1):
        return int(token)
    second = evalRPN(tokens)
    first = evalRPN(tokens)
    if token == "+":
        return int(first + second)
    if token == "-":
        return int(first - second)
    if token == "/":
        return int(first / second)
    if token == "*":
        return int(first * second)


if __name__ == '__main__':
    assert 9 == evalRPN(['2', '1', '+', '3', '*'])
    assert 6 == evalRPN(['4', '13', '5', '/', '+'])
    assert 22 == evalRPN(['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'])
