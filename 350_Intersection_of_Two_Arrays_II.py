from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    output = []
    nums1.sort()
    nums2.sort()

    first = 0
    second = 0

    while first < len(nums1) and second < len(nums2):
        if nums1[first] == nums2[second]:
            output.append(nums1[first])
            first += 1
            second += 1
        elif nums1[first] > nums2[second]:
            second += 1
        else:
            first += 1

    return output


if __name__ == '__main__':
    assert [2, 2] == intersect([1, 2, 2, 1], [2, 2])
    assert [4, 9] == intersect([4, 9, 5], [9, 4, 9, 8, 4])

