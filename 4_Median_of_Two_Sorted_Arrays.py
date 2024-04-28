from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    size = len(nums1) + len(nums2)
    middle = (size + 1) // 2

    left, right = 0, len(nums1)

    while left <= right:
        mid1 = (left + right) // 2
        mid2 = middle - mid1

        nums1_left = nums1[mid1 - 1] if mid1 - 1 >= 0 else float('-inf')
        nums1_right = nums1[mid1] if mid1 < len(nums1) else float('inf')
        nums2_left = nums2[mid2 - 1] if mid2 - 1 >= 0 else float('-inf')
        nums2_right = nums2[mid2] if mid2 < len(nums2) else float('inf')

        if nums1_left <= nums2_right and nums2_left <= nums1_right:
            if size % 2 == 0:
                return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            else:
                return max(nums1_left, nums2_left)
        elif nums1_left > nums2_right:
            right = mid1 - 1
        else:
            left = mid1 + 1

    return -1


if __name__ == '__main__':
    assert 2.0 == findMedianSortedArrays([1, 3], [2])
    assert 2.5 == findMedianSortedArrays([1, 2], [3, 4])
