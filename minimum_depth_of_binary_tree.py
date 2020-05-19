from algorithm.treenode import TreeNode
from sys import maxsize

# https://leetcode.com/problems/minimum-depth-of-binary-tree/
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def dfs(root: TreeNode, depth=0) -> int:
            if root is None:
                return maxsize

            depth += 1
            if root.left is None and root.right is None:
                return depth
            return min(dfs(root.left, depth), dfs(root.right, depth))

        # 例外処理
        if root is None:
            return 0
        return dfs(root)