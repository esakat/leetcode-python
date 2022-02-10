#
# @lc app=leetcode id=1441 lang=python3
#
# [1441] Build an Array With Stack Operations
#

# @lc code=start
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i = 1
        index = 0
        ope = []

        pop_count = 0

        while i <= n:
            ope.append("Push")
            if i == target[index]:
                index += 1
                if index >= len(target):
                    break
            else:
                ope.append("Pop")

            i += 1

        return ope
# @lc code=end

