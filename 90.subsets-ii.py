#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

import copy
from typing import List

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = [[]]
        nums = sorted(nums)

        def backtracking(length: int, index: int, currentSubset: List[int]):
            if len(currentSubset) == length and currentSubset not in res:
                res.append(currentSubset)
                return
            
            for i in range(index, len(nums)):
                newCurrentSubset = currentSubset[:]
                newCurrentSubset.append(nums[i])
                backtracking(length, i+1, newCurrentSubset)

        

        for length in range(1, len(nums)+1):
            backtracking(length, 0, [])
        return res


        
# @lc code=end

