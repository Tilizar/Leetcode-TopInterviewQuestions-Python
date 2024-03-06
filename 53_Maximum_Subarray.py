from typing import List


def maxSubArray(nums: List[int]) -> int:
    maximum = nums[0]
    amount = 0

    for num in nums:
        if amount < 0:
            amount = 0
        amount += num
        maximum = max(maximum, amount)

    return maximum


if __name__ == '__main__':
    assert 6 == maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert 1 == maxSubArray([1])
    assert 23 == maxSubArray([5, 4, -1, 7, 8])
