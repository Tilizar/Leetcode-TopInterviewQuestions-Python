from typing import List, Optional

from utils.TreeNode import TreeNode


def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def populate(left_index: int, right_index: int) -> Optional[TreeNode]:
        if left_index > right_index:
            return None
        mid_index = left_index + (right_index - left_index) // 2
        return TreeNode(
            nums[mid_index],
            left=populate(left_index, mid_index - 1),
            right=populate(mid_index + 1, right_index)
        )

    return populate(0, len(nums) - 1)


if __name__ == '__main__':
    first = TreeNode(0, left=TreeNode(-10, right=TreeNode(-3)), right=TreeNode(5, right=TreeNode(9)))

    assert first == sortedArrayToBST([-10, -3, 0, 5, 9])

    second = TreeNode(1, right=TreeNode(3))

    assert second == sortedArrayToBST([1, 3])
