from typing import List

# https://leetcode.com/problems/word-break/
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        s_list = list(s)

        def helper(start: int, memo: List[bool]) -> bool:
            nonlocal s_list, wordSet
            if start == len(s_list):
                return True

            if memo[start] is not None:
                return memo[start]

            end = start + 1
            while end <= len(s_list):
                if "".join(s_list[start:end]) in wordSet and helper(end, memo):
                    memo[start] = True
                    return True

                memo[start] = False
                end += 1

        return helper(0, [None] * len(s))
