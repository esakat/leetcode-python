#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(now: 'Node', depth: int) -> int:
            tmp = depth
            for c in now.children:
                tmp = max(tmp, dfs(c, depth+1))
            return tmp

        if root is None:
            return 0

        return dfs(root, 1)          
# @lc code=end

