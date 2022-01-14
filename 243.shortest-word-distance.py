
#
# @lc app=leetcode id=243 lang=python3
#
# [243] Shortest Word Distance
#

from typing import List


# @lc code=start
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        beforeWord1Pos = -1
        beforeWord2Pos = -1
        ans = 1000000000

        for i, word in enumerate(wordsDict):
            if word == word1:
                if beforeWord2Pos >= 0:
                    ans = min(ans, i - beforeWord2Pos)
                beforeWord1Pos = i
            elif word == word2:
                if beforeWord1Pos >= 0:
                    ans = min(ans, i - beforeWord1Pos)
                beforeWord2Pos = i               

        return ans

# @lc code=end
 
        