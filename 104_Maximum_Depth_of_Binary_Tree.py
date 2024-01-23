from typing import Optional

from utils.TreeNode import TreeNode


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


if __name__ == '__main__':
    first = TreeNode(
        3,
        left=TreeNode(9),
        right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    )
    assert 3 == maxDepth(first)

    second = TreeNode(1, right=TreeNode(2))
    assert 2 == maxDepth(second)
