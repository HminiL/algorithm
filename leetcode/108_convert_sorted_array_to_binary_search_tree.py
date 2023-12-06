"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
108. Convert Sorted Array to Binary Search Tree
easy
Binary Search Tree
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2

        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1 :])

        return node


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    if not p or not q:
        return p == q
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == "__main__":
    s1 = Solution()
    assert is_same_tree(
        s1.sortedArrayToBST([-10, -3, 0, 5, 9]),
        TreeNode(0, TreeNode(-10, None, TreeNode(-3)), TreeNode(5, None, TreeNode(9))),
    ) or is_same_tree(
        s1.sortedArrayToBST([-10, -3, 0, 5, 9]),
        TreeNode(0, TreeNode(-3, TreeNode(-10), None), TreeNode(9, TreeNode(5), None)),
    ), s1.sortedArrayToBST(
        [-10, -3, 0, 5, 9]
    )

    s2 = Solution()
    assert is_same_tree(
        s2.sortedArrayToBST([1, 3]), TreeNode(3, TreeNode(1))
    ) or is_same_tree(
        s2.sortedArrayToBST([1, 3]), TreeNode(1, None, TreeNode(3))
    ), s2.sortedArrayToBST(
        [1, 3]
    )
