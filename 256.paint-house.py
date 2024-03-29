#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#

from typing import List


# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # dp = [[0] * 3 for i in range(len(costs))]
        # dp[0][0] = costs[0][0]
        # dp[0][1] = costs[0][1]
        # dp[0][2] = costs[0][2]
        # for i in range(1, len(costs)):
        #     dp[i][0] = costs[i][0] + min(dp[i-1][1], dp[i-1][2])
        #     dp[i][1] = costs[i][1] + min(dp[i-1][0], dp[i-1][2])
        #     dp[i][2] = costs[i][2] + min(dp[i-1][0], dp[i-1][1])
        
        # return min(dp[len(costs)-1][0], dp[len(costs)-1][1], dp[len(costs)-1][2])

        # 基本的な動的計画法、久々にといたから一瞬悩んだけどそんなむずくなかったわ
        # 上記は自分で出した答え、下は解答ページ見ながら空間計算量をO(1)にしたもの

        dp = [costs[0][0], costs[0][1], costs[0][2]]
        for i in range(1, len(costs)):
            temp = dp[:]
            dp[0] = costs[i][0] + min(temp[1], temp[2])
            dp[1] = costs[i][1] + min(temp[0], temp[2])
            dp[2] = costs[i][2] + min(temp[0], temp[1])

        return min(dp[0], dp[1], dp[2])



# @lc code=end

