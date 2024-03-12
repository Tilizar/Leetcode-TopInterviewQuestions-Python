from typing import List


def sortColors(nums: List[int]) -> None:
    left, right = 0, len(nums) - 1
    cursor = 0
    
    def swap(i: int, j: int):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    while cursor <= right:
        if nums[cursor] == 0:
            swap(left, cursor)
            left += 1
            cursor += 1
        elif nums[cursor] == 1:
            cursor += 1
        else:
            swap(right, cursor)
            right -= 1


if __name__ == '__main__':
    first = [2, 0, 2, 1, 1, 0]
    sortColors(first)
    assert [0, 0, 1, 1, 2, 2] == first

    second = [2, 0, 1]
    sortColors(second)
    assert [0, 1, 2] == second
