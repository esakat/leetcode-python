#
# @lc app=leetcode id=277 lang=python3
#
# [277] Find the Celebrity
#

# @lc code=start
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:

        for i in range(n):
            flag = True
            for j in range(n):
                if i == j:
                    continue
                if knows(i, j):
                    flag = False
                    break
                if not knows(j, i):
                    flag = False
                    break
            if flag:
                return i


        return -1

# @lc code=end

