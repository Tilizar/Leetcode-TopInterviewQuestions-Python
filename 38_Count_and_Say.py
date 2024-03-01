def countAndSay(n: int) -> str:
    if n == 1:
        return '1'

    prev = countAndSay(n - 1)

    count = 0
    current = prev[0]
    output = ''

    for c in prev:
        if c == current:
            count += 1
        else:
            output += str(count) + current
            count = 1
            current = c

    output += str(count) + current

    return output


if __name__ == '__main__':
    assert '1' == countAndSay(1)
    assert '1211' == countAndSay(4)
