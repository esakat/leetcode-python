#
# @lc app=leetcode id=2119 lang=python3
#
# [2119] A Number After a Double Reversal
#

# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        
        # 例外処理
        if num == 0:
            return True
        
        start = str(num)
        tmp = start[::-1]
        tmp = tmp.lstrip('0')
        end = tmp[::-1]
        end = end.lstrip('0')
        
        return start == end
        
# @lc code=end

