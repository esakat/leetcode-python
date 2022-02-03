#
# @lc app=leetcode id=888 lang=python3
#
# [888] Fair Candy Swap
#

# @lc code=start
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        setB = set(bobSizes)
        for x in aliceSizes:
            if x + (sumB - sumA) / 2 in setB:
                return [x, x + (sumB - sumA) // 2] 

        # 数学問題だった
# @lc code=end

