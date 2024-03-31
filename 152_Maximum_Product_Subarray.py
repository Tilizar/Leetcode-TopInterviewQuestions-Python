from typing import List


def maxProduct(nums: List[int]) -> int:
    output, max_product, min_product = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        new_max = max_product * nums[i]
        new_min = min_product * nums[i]
        max_product = max(new_max, new_min, nums[i])
        min_product = min(new_max, new_min, nums[i])
        output = max(output, max_product)

    return output


if __name__ == '__main__':
    assert 6 == maxProduct([2, 3, -2, 4])
    assert 0 == maxProduct([-2, 0, -1])
