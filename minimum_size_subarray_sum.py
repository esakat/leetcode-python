from typing import List
from sys import maxsize

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        sum = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            sum[i+1] += sum[i] + nums[i]
        l = 0
        r = 0
        now = 0
        length = maxsize
        while l < len(sum) and r < len(sum):
            if now >= s:
                length = min(length, r-l)
                if l < len(sum)-1:
                    l += 1
                else:
                    break
                now = sum[r] - sum[l]
            else:
                if r < len(sum)-1:
                    r += 1
                else:
                    break
                now = sum[r] - sum[l]

        if length == maxsize:
            length = 0

        return length
