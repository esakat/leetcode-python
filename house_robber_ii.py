from typing import List

# https://leetcode.com/problems/house-robber-ii/
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        ptn1 = nums[:-1]
        ptn2 = nums[1:]

        dp1 = [[0] * 2 for i in range(len(nums))]
        dp2 = [[0] * 2 for i in range(len(nums))]

        for i in range(len(ptn1)):
            dp1[i + 1][1] = max(dp1[i + 1][1], dp1[i][0] + ptn1[i])
            dp1[i + 1][0] = max(dp1[i + 1][0], dp1[i][1], dp1[i][0])
            dp2[i + 1][1] = max(dp2[i + 1][1], dp2[i][0] + ptn2[i])
            dp2[i + 1][0] = max(dp2[i + 1][0], dp2[i][1], dp2[i][0])

        return max(dp1[-1][1], dp1[-1][0], dp2[-1][1], dp2[-1][0])