from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    output = []
    subset = []

    def dfs(index):
        if index < len(nums):
            dfs(index + 1)
            subset.append(nums[index])
            dfs(index + 1)
            subset.pop()
        else:
            output.append(subset.copy())

    dfs(0)

    return output


if __name__ == '__main__':
    assert [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]] == subsets([1, 2, 3])
    assert [[], [0]] == subsets([0])
