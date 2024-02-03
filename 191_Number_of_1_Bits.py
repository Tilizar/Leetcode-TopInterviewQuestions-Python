def hammingWeight(n: int) -> int:
    output = 0

    for i in range(32):
        bit = (n >> i) & 1
        if bit == 1:
            output += 1

    return output


if __name__ == '__main__':
    assert 3 == hammingWeight(11)
    assert 1 == hammingWeight(128)
    assert 31 == hammingWeight(4294967293)
