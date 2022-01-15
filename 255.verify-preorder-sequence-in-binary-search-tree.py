#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#

from typing import List


# @lc code=start
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        low = -1
        for p in preorder:
            if p < low:
                return False
            while len(stack) > 0 and p > stack[-1]:
                low = stack.pop()
            stack.append(p)
        return True


# わからんから解答みた。
# 一応流れは追って理解したけど、よくわかってない。
# いきがけ順だとそういう法則ある？


# @lc code=end

