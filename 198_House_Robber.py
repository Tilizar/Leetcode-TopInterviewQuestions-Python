from typing import List


def rob(nums: List[int]) -> int:
    prev, before_prev = 0, 0

    for num in nums:
        new_max = max(num + before_prev, prev)
        before_prev = prev
        prev = new_max

    return prev


if __name__ == '__main__':
    assert 4 == rob([1, 2, 3, 1])
    assert 12 == rob([2, 7, 9, 3, 1])
