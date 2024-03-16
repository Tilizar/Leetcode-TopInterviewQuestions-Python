from typing import Optional

from utils.TreeNode import TreeNode


def isValidBST(root: Optional[TreeNode]) -> bool:
    stack = []
    current = root
    prev = None

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if prev and current.val <= prev.val:
            return False
        prev = current
        current = current.right

    return True


if __name__ == '__main__':
    assert isValidBST(TreeNode(2, left=TreeNode(1), right=TreeNode(3)))
    assert not isValidBST(TreeNode(5, left=TreeNode(1), right=TreeNode(4, left=TreeNode(3), right=TreeNode(6))))
