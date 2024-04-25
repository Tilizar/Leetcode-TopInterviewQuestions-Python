from typing import List


def wiggleSort(nums: List[int]) -> None:
    sorted = nums.copy()
    sorted.sort()
    j = len(nums) - 1

    for i in range(1, len(nums), 2):
        nums[i] = sorted[j]
        j -= 1

    for i in range(0, len(nums), 2):
        nums[i] = sorted[j]
        j -= 1


def case_1():
    array = [1, 5, 1, 1, 6, 4]
    wiggleSort(array)
    expected = [1, 6, 1, 5, 1, 4]
    assert expected == array


def case_2():
    array = [1, 3, 2, 2, 3, 1]
    wiggleSort(array)
    expected = [2, 3, 1, 3, 1, 2]
    assert expected == array


if __name__ == '__main__':
    case_1()
    case_2()
