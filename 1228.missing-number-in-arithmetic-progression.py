#
# @lc app=leetcode id=1228 lang=python3
#
# [1228] Missing Number In Arithmetic Progression
#

# @lc code=start
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        sabun = arr[1]-arr[0]
        for i in range(2, len(arr)):
            if sabun < 0:
                if arr[i] - arr[i-1] < sabun:
                    return arr[i-1] + sabun
            else:
                if arr[i] - arr[i-1] > sabun:
                    return arr[i-1] + sabun
        
        return arr[0] + (sabun // 2)

        
# @lc code=end

