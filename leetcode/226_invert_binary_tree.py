"""
https://leetcode.com/problems/invert-binary-tree/
226. Invert Binary Tree
easy
Tree
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
        while stack:
            parent = stack.pop()
            if parent.left and parent.right:
                parent.left, parent.right = parent.right, parent.left
                stack.append(parent.left)
                stack.append(parent.right)
        return root


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p or not q:
        return p == q
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    s1 = Solution()
    assert is_same_tree(
        s1.invertTree(
            TreeNode(
                4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)),
            )
        ),
        TreeNode(
            4,
            TreeNode(7, TreeNode(9), TreeNode(6)),
            TreeNode(2, TreeNode(3), TreeNode(1)),
        ),
    ), s1.invertTree(
        TreeNode(
            4,
            TreeNode(2, TreeNode(1), TreeNode(3)),
            TreeNode(7, TreeNode(6), TreeNode(9)),
        )
    )

    s2 = Solution()
    assert is_same_tree(
        s2.invertTree(TreeNode(2, TreeNode(1), TreeNode(3))),
        TreeNode(2, TreeNode(3), TreeNode(1)),
    ), s2.invertTree(TreeNode(2, TreeNode(1), TreeNode(3)))

    s3 = Solution()
    assert is_same_tree(s3.invertTree(TreeNode()), TreeNode()), s3.invertTree(
        TreeNode()
    )
