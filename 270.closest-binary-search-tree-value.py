#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

from typing import Optional


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        def reccursive(now: Optional[TreeNode], res: int) -> int:
            if now is None:
                return res
            
            if abs(now.val - target) < abs(res - target):
                res = now.val
            
            tmp = reccursive(now.left, res)
            if abs(tmp - target) < abs(res - target):
                res = tmp
            
            tmp = reccursive(now.right, res)
            if abs(tmp - target) < abs(res - target):
                res = tmp

            return res
            

        return reccursive(root, root.val)
# @lc code=end

