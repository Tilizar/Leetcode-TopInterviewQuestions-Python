from typing import List


def majorityElement(nums: List[int]) -> int:
    majority = 0
    counter = 0

    for num in nums:
        if counter == 0:
            majority = num
        counter += 1 if majority == num else -1

    return majority


if __name__ == '__main__':
    assert 3 == majorityElement([3, 2, 3])
    assert 2 == majorityElement([2, 2, 1, 1, 1, 2, 2])
