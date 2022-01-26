#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'Optional[TreeNode]':


        flag = False
        complete = False
        ans = None

        def inorderTravase(now: TreeNode):
            nonlocal flag, ans, complete
            if now.left is not None:
                inorderTravase(now.left)
            if flag and not complete:
                ans = now
                complete = True
                print(ans)
            if now is p:
                flag = True
            if now.right is not None:
                inorderTravase(now.right)

        inorderTravase(root)
        return ans


# @lc code=end

