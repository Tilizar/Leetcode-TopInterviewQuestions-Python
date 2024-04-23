from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    lengths = [1] * len(nums)
    output = 1

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                current_length = max(lengths[i], lengths[j] + 1)
                lengths[i] = current_length
                output = max(output, current_length)

    return output


if __name__ == '__main__':
    assert 4 == lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
    assert 4 == lengthOfLIS([0, 1, 0, 3, 2, 3])
    assert 1 == lengthOfLIS([7, 7, 7, 7, 7, 7, 7])
