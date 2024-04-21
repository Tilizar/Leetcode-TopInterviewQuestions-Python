from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    pointer = 0
    while True:
        slow = nums[slow]
        pointer = nums[pointer]
        if slow == pointer:
            break

    return pointer


if __name__ == '__main__':
    assert 2 == findDuplicate([1, 3, 4, 2, 2])
    assert 3 == findDuplicate([3, 1, 3, 4, 2])
    assert 3 == findDuplicate([3, 3, 3, 3, 3])
