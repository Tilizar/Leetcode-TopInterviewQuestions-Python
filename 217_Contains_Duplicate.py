from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    cache = set()

    for num in nums:
        if num in cache:
            return True
        cache.add(num)

    return False


if __name__ == '__main__':
    assert containsDuplicate([1, 2, 3, 1])
    assert not containsDuplicate([1, 2, 3, 4])
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
