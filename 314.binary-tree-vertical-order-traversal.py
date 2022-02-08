#
# @lc app=leetcode id=314 lang=python3
#
# [314] Binary Tree Vertical Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = dict()
        
        queue = []
        if root is not None:
            queue.append((root, 0))

        while len(queue) > 0:
            (node, now) = queue[0]
            queue = queue[1:]
            if now in mp:
                mp[now].append(node.val)
            else:
                mp[now] = [node.val]
            if node.left is not None:
                queue.append((node.left, now-1))
            if node.right is not None:
                queue.append((node.right, now+1))

        # def dfs(node: Optional[TreeNode], now: int):
        #     if now in mp:
        #         mp[now].append(node.val)
        #     else:
        #         mp[now] = [node.val]
        #     if node.left is not None:
        #         dfs(node.left, now-1)
        #     if node.right is not None:
        #         dfs(node.right, now+1)

        # dfs(root, 0)

        minVal = sys.maxsize
        for k in mp.keys():
            minVal = min(minVal, k)
        minVal = abs(minVal)
        
        ans = [[] for v in range(len(mp))]

        for k, v in mp.items():
            ans[k+minVal] = v

        return ans
# @lc code=end

