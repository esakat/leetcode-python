#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        ret = []
        stack = []
        stack.append(root)
        while len(stack) > 0:
            now = stack.pop()
            if now == None:
                continue
            ret.append(now.val)
            stack.append(now.left)
            stack.append(now.right)

        def srt(v):
            return abs(v - target)

        
        nret = sorted(ret, key=srt)

        return nret[:k]

# @lc code=end

