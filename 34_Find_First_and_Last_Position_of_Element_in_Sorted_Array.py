from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    left_start, left_end = 0, len(nums) - 1
    right_start, right_end = 0, len(nums) - 1
    left_index, right_index = -1, -1

    while left_start <= left_end:
        mid_index = (left_start + left_end) // 2
        mid = nums[mid_index]
        if target > mid:
            left_start = mid_index + 1
        else:
            if mid == target:
                left_index = mid_index
            left_end = mid_index - 1

    while right_start <= right_end:
        mid_index = (right_start + right_end) // 2
        mid = nums[mid_index]
        if target >= mid:
            if mid == target:
                right_index = mid_index
            right_start = mid_index + 1
        else:
            right_end = mid_index - 1

    return [left_index, right_index]


if __name__ == '__main__':
    assert [3, 4] == searchRange([5, 7, 7, 8, 8, 10], 8)
    assert [-1, -1] == searchRange([5, 7, 7, 8, 8, 10], 6)
    assert [-1, -1] == searchRange([], 0)
