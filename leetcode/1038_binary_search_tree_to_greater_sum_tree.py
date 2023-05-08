"""
https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
1038. Binary Search Tree to Greater Sum Tree
Medium
Binary Search Tree
"""
from dataclasses import dataclass


# Definition for a binary tree node.
@dataclass
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        val: int = 0
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root


if __name__ == '__main__':
    pass
