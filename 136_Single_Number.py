from typing import List


def singleNumber(nums: List[int]) -> int:
    nums.sort()
    output = 0
    even = True
    for num in nums:
        if even:
            output += num
        else:
            output -= num
        even = not even

    return output


if __name__ == '__main__':
    assert 1 == singleNumber([2, 2, 1])
    assert 4 == singleNumber([4, 1, 2, 1, 2])
    assert 1 == singleNumber([1])
