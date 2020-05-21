from typing import List

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        now = prices[0]
        pool = 0
        profit = 0
        buy = True

        for i,p in enumerate(prices):
            if i == 0:
                continue

            if buy:
                if p > now:
                    buy = False
                    pool = now
            else:
                if p < now:
                    buy = True
                    profit += now - pool
                    pool = 0

            now = p

        if not buy:
            profit += now - pool

        return profit
