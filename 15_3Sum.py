from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    output = []
    nums.sort()

    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum > 0:
                right -= 1
            elif sum < 0:
                left += 1
            else:
                output.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return output


if __name__ == '__main__':
    assert [[-1, -1, 2], [-1, 0, 1]] == threeSum([-1, 0, 1, 2, -1, -4])
    assert [] == threeSum([0, 1, 1])
    assert [[0, 0, 0]] == threeSum([0, 0, 0])
