from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)

        i = 1
        while i < len(s):
            print(s, i)
            f = s[:i]
            if f in wordSet:
                s = s[i:]
                i == 1
            else:
                i += 1

        return len(s) == 0
