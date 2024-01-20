from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int):
    cursor = m + n - 1

    while m > 0 and n > 0:
        left, right = nums1[m - 1], nums2[n - 1]
        if nums1[m - 1] > nums2[n - 1]:
            nums1[cursor] = left
            m -= 1
        else:
            nums1[cursor] = right
            n -= 1
        cursor -= 1

    while n > 0:
        nums1[cursor] = nums2[n - 1]
        n -= 1
        cursor -= 1


if __name__ == '__main__':
    input = [1, 2, 3, 0, 0, 0]
    merge(input, 3, [2, 5, 6], 3)
    assert [1, 2, 2, 3, 5, 6] == input
