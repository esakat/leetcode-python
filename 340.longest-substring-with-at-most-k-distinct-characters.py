#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans = 0
        i = j = 0
        mp = dict()
        while i < len(s):
            if len(mp) <= k and j < len(s):
                if s[j] in mp:
                    mp[s[j]] += 1
                else:
                    mp[s[j]] = 1
                j += 1
            else:
                if mp[s[i]] == 1:
                    del mp[s[i]]
                else:
                    mp[s[i]] -= 1
                i += 1

            if len(mp) <= k:
                ans = max(ans, j-i)
        
        return ans

# @lc code=end

