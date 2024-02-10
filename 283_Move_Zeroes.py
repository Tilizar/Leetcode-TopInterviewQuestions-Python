from typing import List


def moveZeroes(nums: List[int]):
    slow, fast = 0, 0

    while fast < len(nums):
        if nums[fast] != 0:
            if fast != slow:
                nums[slow] = nums[fast]
                nums[fast] = 0
            slow += 1
        fast += 1


if __name__ == '__main__':
    first = [0, 1, 0, 3, 12]
    moveZeroes(first)
    assert [1, 3, 12, 0, 0] == first

    second = [0]
    moveZeroes(second)
    assert [0] == second
