from typing import List
from sys import maxsize
from bisect import bisect_left

# https://leetcode.com/problems/longest-increasing-subsequence/
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [maxsize] * 100000
        ans[0] = -maxsize

        for v in nums:
            index = bisect_left(ans, v)
            ans[index] = v

        ret = -1
        for v in ans:
            if v == maxsize:
                break
            ret += 1

        return ret
