from typing import List


def canJump(nums: List[int]) -> bool:
    target_pos = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= target_pos:
            target_pos = i

    return target_pos == 0


if __name__ == '__main__':
    assert canJump([2, 3, 1, 1, 4])
    assert not canJump([3, 2, 1, 0, 4])
