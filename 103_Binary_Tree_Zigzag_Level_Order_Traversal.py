from typing import Optional, List

from utils.TreeNode import TreeNode


def zigzagLevelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    output = []
    stack = []
    if root:
        stack.append(root)
    left_to_right = True

    while stack:
        level = []
        stack_size = len(stack)
        for i in range(stack_size):
            current = stack.pop(stack_size - 1 - i)
            if current:
                level.append(current.val)
                if left_to_right:
                    stack.append(current.left)
                    stack.append(current.right)
                else:
                    stack.append(current.right)
                    stack.append(current.left)
        left_to_right = not left_to_right
        if level:
            output.append(level)

    return output


if __name__ == '__main__':
    first = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    assert [[3], [20, 9], [15, 7]] == zigzagLevelOrder(first)
    assert [[1]] == zigzagLevelOrder(TreeNode(1))
    assert [] == zigzagLevelOrder(None)
