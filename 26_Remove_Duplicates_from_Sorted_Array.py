from typing import List


def removeDuplicates(nums: List[int]) -> int:
    pointer = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[pointer] = nums[i]
            pointer += 1

    return pointer


if __name__ == '__main__':
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    output = removeDuplicates(nums)
    print(nums)
    print(output)