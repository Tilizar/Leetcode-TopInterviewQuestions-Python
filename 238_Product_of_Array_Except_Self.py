from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)

    for i in range(len(nums)):
        left = 1 if i == 0 else prefix[i - 1]
        prefix[i] = left * nums[i]

    for i in range(len(nums) - 1, -1, -1):
        right = 1 if i == len(nums) - 1 else postfix[i + 1]
        postfix[i] = right * nums[i]

    output = [1] * len(nums)

    for i in range(len(nums)):
        left = 1 if i == 0 else prefix[i - 1]
        right = 1 if i == len(nums) - 1 else postfix[i + 1]
        output[i] = left * right

    return output


if __name__ == '__main__':
    assert [24, 12, 8, 6] == productExceptSelf([1, 2, 3, 4])
    assert [0, 0, 9, 0, 0] == productExceptSelf([-1, 1, 0, -3, 3])
