from typing import List


def trap(height: List[int]) -> int:
    amount = 0

    left, right = 0, len(height) - 1
    left_max, right_max = -1, -1

    while left <= right:
        if left_max < right_max:
            left_max = max(left_max, height[left])
            amount += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            amount += right_max - height[right]
            right -= 1

    return amount


if __name__ == '__main__':
    assert 6 == trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert 9 == trap([4, 2, 0, 3, 2, 5])
