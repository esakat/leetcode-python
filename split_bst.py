from typing import List
from algorithm.treenode import TreeNode

# https://leetcode.com/problems/split-bst/
class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:

        if root is None:
            return None, None
        elif root.val <= V:
            bns = self.splitBST(root.right, V)
            root.right = bns[0]
            return root, bns[1]
        else:
            bns = self.splitBST(root.left, V)
            root.left = bns[1]
            return bns[0], root
