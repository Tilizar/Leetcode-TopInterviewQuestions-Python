from typing import Optional

from utils.TreeNode import TreeNode


def isSymmetric(root: Optional[TreeNode]) -> bool:

    def compare(left: Optional[TreeNode], right: Optional[TreeNode]):
        if not left and not right:
            return True
        if not left or not right:
            return False

        return left.val == right.val and compare(left.left, right.right) and compare(left.right, right.left)

    return compare(root.left, root.right)


if __name__ == '__main__':
    first = TreeNode(
        1,
        right=TreeNode(2, left=TreeNode(3), right=TreeNode(4)),
        left=TreeNode(2, left=TreeNode(4), right=TreeNode(3))
    )
    assert isSymmetric(first)

    second = TreeNode(
        1,
        right=TreeNode(2, right=TreeNode(3)),
        left=TreeNode(2, right=TreeNode(3))
    )
    assert not isSymmetric(second)
