from utils.TreeNode import TreeNode


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root.val == p.val or root.val == q.val:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    return root if left and right else left or right


if __name__ == '__main__':
    tree = TreeNode(3,
                    left=TreeNode(5, left=TreeNode(6), right=TreeNode(2, left=TreeNode(7), right=TreeNode(4))),
                    right=TreeNode(1, left=TreeNode(0), right=TreeNode(8))
                    )
    assert 3 == lowestCommonAncestor(tree, TreeNode(5), TreeNode(1)).val
    assert 5 == lowestCommonAncestor(tree, TreeNode(5), TreeNode(4)).val
    assert 1 == lowestCommonAncestor(TreeNode(1, left=TreeNode(2)), TreeNode(1), TreeNode(2)).val
