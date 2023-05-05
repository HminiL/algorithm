"""
https://leetcode.com/problems/longest-univalue-path/
687. Longest Univalue Path
Medium
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            self.result = max(self.result, left + right)
            return max(left, right)

        dfs(root)
        return self.result


class Solution2:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, res):
            if not node:
                return 0
            left = dfs(node.left, res)
            right = dfs(node.right, res)

            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            res[0] = max(res[0], left + right)
            return max(left, right)

        if not root:
            return 0
        res = [0]
        dfs(root, res)
        return res[0]


class Solution3:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node, res):
            left, right = 0, 0
            if node.left:
                left = dfs(node.left, res)
                left = left + 1 if node.val == node.left.val else 0
            if node.right:
                right = dfs(node.right, res)
                right = right + 1 if node.val == node.right.val else 0
            res[0] = max(res[0], left + right)
            return max(left, right)

        if not root:
            return 0
        res = [0]
        dfs(root, res)
        return res[0]


if __name__ == '__main__':
    # s1 = Solution()
    # assert s1.longestUnivaluePath(
    #     TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))) == 2, \
    #     s1.longestUnivaluePath(TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5))))
    # s2 = Solution()
    # assert s2.longestUnivaluePath(
    #     TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5)))) == 2, \
    #     s2.longestUnivaluePath(TreeNode(1, TreeNode(4, TreeNode(4), TreeNode(4)), TreeNode(5, None, TreeNode(5))))
    # s3 = Solution2()
    # assert s3.longestUnivaluePath(
    #     TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))) == 2, \
    #     s3.longestUnivaluePath(TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5))))
    s4 = Solution3()
    assert s4.longestUnivaluePath(
        TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5)))) == 2, \
        s4.longestUnivaluePath(TreeNode(5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5))))
