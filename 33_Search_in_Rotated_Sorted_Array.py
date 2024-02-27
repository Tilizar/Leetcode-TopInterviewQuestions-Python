from typing import List


def search(nums: List[int], target: int) -> int:
    if nums[0] == target:
        return 0

    search_in_shifted_part = target < nums[0]

    start, end = 0, len(nums) - 1

    while start <= end:
        index = start + (end - start) // 2

        if nums[index] == target:
            return index

        if search_in_shifted_part and nums[index] >= nums[0]:
            start = index + 1
            continue
        if not search_in_shifted_part and nums[index] < nums[0]:
            end = index - 1
            continue

        if nums[index] < target:
            start = index + 1
        else:
            end = index - 1

    return -1


if __name__ == '__main__':
    assert 4 == search([4, 5, 6, 7, 0, 1, 2], 0)
    assert -1 == search([4, 5, 6, 7, 0, 1, 2], 3)
    assert -1 == search([1], 0)
