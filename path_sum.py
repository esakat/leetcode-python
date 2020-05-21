# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from algorithm.treenode import TreeNode

# https://leetcode.com/problems/path-sum/
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        # helper
        def dfs(root: TreeNode, now: int) -> bool:
            nonlocal sum

            if root == None:
                return False

            now += root.val

            if root.left == None and root.right == None:
                # This is Leaf
                return sum == now

            return dfs(root.left, now) or dfs(root.right, now)

        return dfs(root, 0)
