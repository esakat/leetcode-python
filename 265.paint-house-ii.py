#
# @lc app=leetcode id=265 lang=python3
#
# [265] Paint House II
#

from typing import List
import sys


# @lc code=start
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        k = len(costs[0])
        n = len(costs)

        dp = [[sys.maxsize] * k for i in costs]
        for i, cost in enumerate(costs[0]):
            dp[0][i] = cost

        for i in range(1, n):
            for j in range(k):
                for l in range(k):
                    if j != l:
                        dp[i][j] = min(dp[i][j], dp[i-1][l] + costs[i][j])
        
        minCost = sys.maxsize
        for v in dp[-1]:
            minCost = min(minCost, v)
        
        return minCost

# O(n・k^2)の解答
# 通った。最適解だとO(n・k)でいけるらしい時間

# @lc code=end
