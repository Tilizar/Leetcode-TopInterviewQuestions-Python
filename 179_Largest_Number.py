from functools import cmp_to_key
from typing import List


def largestNumber(nums: List[int]) -> str:
    def compare(first, second):
        return -1 if first + second > second + first else 1

    nums = sorted(map(str, nums), key=cmp_to_key(compare))
    if nums[0] == '0':
        return '0'
    return ''.join(nums)


if __name__ == '__main__':
    assert '210' == largestNumber([10, 2])
    assert '9534330' == largestNumber([3, 30, 34, 5, 9])
