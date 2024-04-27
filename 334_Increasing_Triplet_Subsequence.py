from typing import List

def increasingTriplet(nums: List[int]) -> bool:
    if len(nums) < 3:
        return False

    first_min = second_min = float('inf')

    for num in nums:
        if num <= first_min:
            first_min = num
        elif num <= second_min:
            second_min = num
        else:
            return True

    return False


if __name__ == '__main__':
    assert increasingTriplet([1, 2, 3, 4, 5])
    assert not increasingTriplet([5, 4, 3, 2, 1])
    assert increasingTriplet([2, 1, 5, 0, 4, 6])
