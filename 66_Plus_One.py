from typing import List


def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits


if __name__ == '__main__':
    assert [1, 2, 4] == plusOne([1, 2, 3])
    assert [4, 3, 2, 2] == plusOne([4, 3, 2, 1])
    assert [1, 0] == plusOne([9])
