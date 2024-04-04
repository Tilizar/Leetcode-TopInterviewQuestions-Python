def trailingZeroes(n: int) -> int:
    output = 0
    while n > 0:
        n //= 5
        output += n
    return output


if __name__ == '__main__':
    assert 0 == trailingZeroes(3)
    assert 1 == trailingZeroes(5)
    assert 0 == trailingZeroes(0)
