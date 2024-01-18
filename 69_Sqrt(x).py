def mySqrt(x: int) -> int:
    value = 0
    left, right = 0, x

    while left <= right:
        mid = left + ((right - left) // 2)
        if mid**2 > x:
            right = mid - 1
        elif mid**2 < x:
            left = mid + 1
            value = mid
        else:
            return mid

    return value


if __name__ == '__main__':
    assert 2 == mySqrt(4)
    assert 2 == mySqrt(8)
