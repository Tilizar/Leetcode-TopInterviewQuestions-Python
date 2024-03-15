def numDecodings(s: str) -> int:
    cache = [0] * (len(s) + 1)
    cache[len(s)] = 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            cache[i] = 0
        else:
            cache[i] = cache[i + 1]

        if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and int(s[i + 1]) <= 6):
            cache[i] += cache[i + 2]

    return cache[0]


if __name__ == '__main__':
    assert 2 == numDecodings('12')
    assert 3 == numDecodings('226')
    assert 0 == numDecodings('06')
