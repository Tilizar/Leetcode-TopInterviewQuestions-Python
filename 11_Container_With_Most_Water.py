from typing import List


def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_area = 0

    while l < r:
        current_area = (r - l) * min(height[l], height[r])
        max_area = max(max_area, current_area)
        if height[l] < height[r]:
            l += 1
        else:
            r -=1

    return max_area


if __name__ == '__main__':
    assert 49 == maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert 1 == maxArea([1, 1])
