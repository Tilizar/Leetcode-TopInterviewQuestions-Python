from typing import List


def findPeakElement(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        left_smaller = mid == 0 or nums[mid] > nums[mid - 1]
        right_smaller = mid == len(nums) - 1 or nums[mid] > nums[mid + 1]
        if left_smaller and right_smaller:
            return mid
        if left_smaller:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == '__main__':
    assert 2 == findPeakElement([1, 2, 3, 1])
    assert 5 == findPeakElement([1, 2, 1, 3, 5, 6, 4])
