#
# @lc app=leetcode id=298 lang=python3
#
# [298] Binary Tree Longest Consecutive Sequence
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from audioop import reverse


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def recursive(node: Optional[TreeNode], parentVal: int, tmp: int, ans: int) -> int:
            if parentVal + 1 == node.val:
                tmp += 1
            else:
                tmp = 1

            ans = max(ans, tmp)
            
            if node.left is not None:
                ans = max(ans, recursive(node.left, node.val, tmp, ans))
            if node.right is not None:
                ans = max(ans, recursive(node.right, node.val, tmp, ans))

            return ans

        return recursive(root, 0, 0, 0)

# @lc code=end

