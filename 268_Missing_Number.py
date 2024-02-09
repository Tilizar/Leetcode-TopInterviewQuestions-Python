from typing import List


def missingNumber(nums: List[int]) -> int:
    full_range_sum = 0
    for i in range(len(nums) + 1):
        full_range_sum += i

    real_range_sum = 0
    for i in range(len(nums)):
        real_range_sum += nums[i]

    return full_range_sum - real_range_sum


if __name__ == '__main__':
    assert 2 == missingNumber([3, 0, 1])
    assert 2 == missingNumber([0, 1])
    assert 8 == missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])
