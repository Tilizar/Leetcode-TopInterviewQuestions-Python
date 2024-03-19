from typing import List, Optional

from utils.TreeNode import TreeNode


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None

    root_inorder_index = inorder.index(preorder[0])
    root = TreeNode(inorder[root_inorder_index])
    root.left = buildTree(preorder[1:root_inorder_index + 1], inorder[:root_inorder_index])
    root.right = buildTree(preorder[root_inorder_index + 1:], inorder[root_inorder_index + 1:])
    return root


if __name__ == '__main__':
    first = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
    assert first == buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert TreeNode(-1) == buildTree([-1], [-1])
