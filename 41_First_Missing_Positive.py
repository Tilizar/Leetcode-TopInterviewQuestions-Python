from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0

    for i in range(len(nums)):
        real_index = abs(nums[i]) - 1
        if real_index < 0 or real_index >= len(nums):
            continue
        if nums[real_index] > 0:
            nums[real_index] *= -1
        elif nums[real_index] == 0:
            nums[real_index] = -(len(nums) + 1)

    for i in range(len(nums)):
        if nums[i] >= 0:
            return i + 1

    return len(nums) + 1


if __name__ == '__main__':
    assert 3 == firstMissingPositive([1, 2, 0])
    assert 2 == firstMissingPositive([3, 4, -1, 1])
    assert 1 == firstMissingPositive([7, 8, 9, 11, 12])
