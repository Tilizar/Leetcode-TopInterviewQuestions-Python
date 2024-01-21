from typing import Optional, List

from utils.TreeNode import TreeNode


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    current = root
    stack = []
    output = []

    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        output.append(current.val)
        current = current.right

    return output


if __name__ == '__main__':
    tree = TreeNode(1, right = TreeNode(2, left = TreeNode(3)))
    assert [1, 3, 2] == inorderTraversal(tree)
