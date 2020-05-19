# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List
from algorithm.treenode import TreeNode

# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        preorderidx = 0

        def travarse(left=0, right=len(inorder)) -> TreeNode:
            nonlocal preorderidx

            if left == right:
                return None

            root_val = preorder[preorderidx]
            root = TreeNode(root_val)
            index = mp[root_val]

            preorderidx += 1
            # build left subtree
            root.left = travarse(left, index)
            # build right subtree
            root.right = travarse(index + 1, right)
            return root

        # inorderのindexを管理する管理する
        mp = {}
        for i, val in enumerate(inorder):
            mp[val] = i

        return travarse()
