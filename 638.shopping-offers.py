#
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#

# @lc code=start
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        needsSet = {p - 1 for p in needs}
        ret = sys.maxsize
        for i in range(2 ** (n*2)):
            buy = set()
            cost = 0
            print("pattern {}: ".format(i), end="")
            for j in range(n*2):  
                if ((i >> j) & 1):
                    if j < n:
                        cost += price[j]
                        buy.add(j)
                    else:
                        cost += special[j-n][n]
                        for k in range(n):
                            buy.add(special[j-n][k])
            if needsSet <= buy:
                ret = min(ret, cost)

        return ret

# @lc code=end

