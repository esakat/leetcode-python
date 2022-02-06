#
# @lc app=leetcode id=657 lang=python3
#
# [657] Robot Return to Origin
#

# @lc code=start
from nis import match


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = 0
        vertical = 0

        for ope in moves:
            if ope == 'U':
                horizontal += 1
            if ope == 'D':
                horizontal -= 1
            if ope == 'R':
                vertical += 1
            if ope == 'L':
                vertical -= 1

        return horizontal == 0 and vertical == 0
 
            
# @lc code=end

