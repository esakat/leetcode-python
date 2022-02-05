#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mp = dict()
        ans = -1
        for v in arr:
            if v in mp:
                mp[v] += 1
            else:
                mp[v] = 1
        
        for k, v in mp.items():
            if k == v:
                ans = max(ans, k)

        return ans
# @lc code=end

