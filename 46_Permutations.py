from typing import List, Set


def permute(nums: List[int]) -> List[List[int]]:
    if len(nums) == 1:
        return [nums[:]]

    output = []

    for i in range(len(nums)):
        num = nums.pop()
        perms = permute(nums)

        for perm in perms:
            perm.append(num)

        output.extend(perms)
        nums.insert(0, num)

    return output


if __name__ == '__main__':
    first = [[1, 2, 3], [2, 1, 3], [3, 1, 2], [1, 3, 2], [2, 3, 1], [3, 2, 1]]
    assert first == permute([1, 2, 3])

    assert [[0, 1], [1, 0]] == permute([0, 1])

    assert [[1]] == permute([1])
