#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(100):
            if 3 ** i == n:
                return True
            elif 3 ** i > n:
                return False
        return False
# @lc code=end

