#
# @lc app=leetcode id=291 lang=python3
#
# [291] Word Pattern II
#

# @lc code=start
class Solution:
    def wordPatternMatch(self, pattern, str):
        self.pMap = dict()
        self.sMap = dict()
        return self.dfs(pattern, 0, str, 0)

    def dfs(self, pattern, i, str, j):
        if len(pattern) == i and len(str) == j:
            return True
        if len(pattern) == i or len(str) == j:
            return False
        
        c = pattern[i]
        insert = False

        for k in range(j, len(str)):
            s = str[j:k+1]
            
            if c in self.pMap and self.pMap[c] != s:
                continue
            if s in self.sMap and self.sMap[s] != c:
                continue
            if not c in self.pMap and not s in self.sMap:
                self.pMap[c] = s
                self.sMap[s] = c
                insert = True

            if self.dfs(pattern, i+1, str, k+1):
                return True

            if insert:
                del self.pMap[c]
                del self.sMap[s]
        
        return False


# @lc code=end

