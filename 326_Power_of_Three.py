def isPowerOfThree(n: int) -> bool:
    return (pow(3, 20) % n) == 0 if n > 0 else False


if __name__ == '__main__':
    assert isPowerOfThree(27)
    assert not isPowerOfThree(0)
    assert not isPowerOfThree(-1)
