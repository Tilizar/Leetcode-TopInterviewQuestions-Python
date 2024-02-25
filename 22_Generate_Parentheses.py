from typing import List


def generateParenthesis(n: int) -> List[str]:
    acc = []

    def populate(opened: int, closed: int, current: str):
        if opened == n and closed == n:
            acc.append(current)
            return

        if opened < n:
            populate(opened + 1, closed, current + '(')
        if closed < n and opened > closed:
            populate(opened, closed + 1, current + ')')

    populate(0, 0, '')

    return acc


if __name__ == '__main__':
    assert ['((()))', '(()())', '(())()', '()(())', '()()()'] == generateParenthesis(3)
    assert ['()'] == generateParenthesis(1)
