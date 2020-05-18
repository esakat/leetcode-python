from typing import List
from sys import maxsize
from bisect import bisect_left
from algorithm.treenode import TreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def construct(left: int, right: int) -> TreeNode:
            if left > right:
                return None

            p = int((left + right)/2)
            if (left + right)%2 == 1:
                p += 1

            root = TreeNode(nums[p])
            root.left = construct(left, p-1)
            root.right = construct(p+1, right)
            return root

        return construct(0, len(nums)-1)
