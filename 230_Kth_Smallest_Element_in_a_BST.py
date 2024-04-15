from typing import Optional

from utils.TreeNode import TreeNode


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    current = root
    stack = []
    counter = 0

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        counter += 1
        if counter == k:
            return current.val
        current = current.right
    return -1


if __name__ == '__main__':
    first = TreeNode(3, left=TreeNode(1, right=TreeNode(2)), right=TreeNode(4))
    assert 1 == kthSmallest(first, 1)

    first = TreeNode(5, left=TreeNode(3, left=TreeNode(2, left=TreeNode(1)), right=TreeNode(4)), right=TreeNode(6))
    assert 3 == kthSmallest(first, 3)
