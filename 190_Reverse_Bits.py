def reverseBits(n: int) -> int:
    output = 0

    for i in range(32):
        bit = (n >> i) & 1
        output |= (bit << (31 - i))

    return output


if __name__ == '__main__':
    assert 964176192 == reverseBits(43261596) # 00111001011110000010100101000000 == reverseBits(00000010100101000001111010011100)
    assert 3221225471 == reverseBits(4294967293) # 10111111111111111111111111111111 == reverseBits(11111111111111111111111111111101)
