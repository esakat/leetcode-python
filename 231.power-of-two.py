#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        binStr = bin(n)[2:]
        return binStr.count('1') == 1 and binStr[0] == '1'
        
# @lc code=end

