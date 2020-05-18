from typing import List
from sys import maxsize
from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for v in range(100000):
            ans.append(maxsize)
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
