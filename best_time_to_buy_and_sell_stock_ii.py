from typing import List
from sys import maxsize

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [[-maxsize] * (len(prices)+1) for i in range(len(prices)+1)]

        profit[0][0] = 0

        for i,p in enumerate(prices):
            for j,v in enumerate(profit[i]):

                if v == -maxsize:
                    break
                else:
                    profit[i+1][j] = max(profit[i+1][j+1], profit[i][j] - v)


