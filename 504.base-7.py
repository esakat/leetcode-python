#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        isMinus = False
        if num < 0:
            isMinus = True
        num = abs(num)

        tmp = []
        while num >= 7:
            amari = str(num % 7)
            tmp.append(amari)
            num = num // 7
        tmp.append(str(num))
        tmp.reverse()
        ans = ""
        if isMinus:
            ans += '-'
        ans += ''.join(tmp)
        return ans

# @lc code=end

