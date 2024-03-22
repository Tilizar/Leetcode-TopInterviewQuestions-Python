from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums_as_set = set(nums)
    output = 0

    for num in nums:
        if num - 1 in nums_as_set:
            continue
        count = 1
        while num + count in nums_as_set:
            count += 1
        output = max(output, count)

    return output


if __name__ == '__main__':
    assert 4 == longestConsecutive([100, 4, 200, 1, 3, 2])
    assert 9 == longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
