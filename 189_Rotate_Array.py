from typing import List


def rotate(nums: List[int], k: int) -> None:
    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

    k %= len(nums)
    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


if __name__ == '__main__':
    first = [1, 2, 3, 4, 5, 6, 7]
    rotate(first, 3)
    assert [5, 6, 7, 1, 2, 3, 4] == first

    second = [-1, -100, 3, 99]
    rotate(second, 2)
    assert [3, 99, -1, -100] == second
