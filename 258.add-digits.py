#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        s = "{}".format(num)

        if len(s) == 1:
            return num
        else:
            nextNum = 0
            for c in s:
                nextNum += int(c)
            return self.addDigits(nextNum)


# @lc code=end

