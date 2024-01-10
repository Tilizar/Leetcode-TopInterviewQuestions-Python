from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    cache = {}

    for index, number in enumerate(nums):
        cached = cache.get(target - number)
        if cached is not None:
            return [cached, index]
        else:
            cache[number] = index

    return []


if __name__ == '__main__':
    assert [0, 1] == twoSum([2, 7, 11, 15], 9)
    assert [1, 2] == twoSum([3, 2, 4], 6)
    assert [0, 1] == twoSum([3, 3], 6)
