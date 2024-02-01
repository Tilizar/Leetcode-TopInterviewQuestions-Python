def titleNumber(columnTitle: str) -> int:
    result = 0

    for i, c in enumerate(reversed(columnTitle)):
        result += 26**i * (ord(c) - ord('A') + 1)

    return result


if __name__ == '__main__':
    assert 1 == titleNumber('A')
    assert 28 == titleNumber('AB')
    assert 701 == titleNumber('ZY')
