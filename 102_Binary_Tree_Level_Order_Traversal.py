from typing import Optional, List

from utils.TreeNode import TreeNode


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    output = []
    stack = []
    if root:
        stack.append(root)

    while stack:
        level = []
        for i in range(len(stack)):
            current = stack.pop(0)
            if current:
                level.append(current.val)
                stack.append(current.left)
                stack.append(current.right)
        if level:
            output.append(level)

    return output


if __name__ == '__main__':
    first = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    assert [[3], [9, 20], [15, 7]] == levelOrder(first)
    assert [[1]] == levelOrder(TreeNode(1))
    assert [] == levelOrder(None)
