#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        st = "{0:b}".format(n)

        beforeone = 0
        ans = 0
        for i, c in enumerate(st):
            if c == '1':
                ans = max(ans, i-beforeone)
                beforeone = i
        
        return ans
# @lc code=end

