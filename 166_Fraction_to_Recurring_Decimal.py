def fractionToDecimal(numerator: int, denominator: int) -> str:
    if numerator == 0:
        return '0'

    output = []
    if (numerator < 0) ^ (denominator < 0):
        output.append('-')
    numerator = abs(numerator)
    denominator = abs(denominator)

    output.append(str(numerator // denominator))
    numerator %= denominator
    if numerator == 0:
        return ''.join(output)

    output.append('.')
    cache = {numerator: len(output)}
    while numerator != 0:
        numerator *= 10
        output.append(str(numerator // denominator))
        numerator %= denominator
        if numerator not in cache:
            cache[numerator] = len(output)
        else:
            output.insert(cache[numerator], '(')
            output.append(')')
            break

    return ''.join(output)


if __name__ == '__main__':
    assert "0.5" == fractionToDecimal(1, 2)
    assert "2" == fractionToDecimal(2, 1)
    assert "0.(012)" == fractionToDecimal(4, 333)
