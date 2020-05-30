from typing import List

# https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # 累積和とhashmapを使ったO(N)の解法
        sum = [0] * (len(nums) + 1)
        mp = {}
        mp[0] = 1
        for i, v in enumerate(nums):
            sum[i+1] = sum[i] + v
            if sum[i+1] in mp:
                mp[sum[i+1]] += 1
            else:
                mp[sum[i+1]] = 1

        count = 0
        for v in sum:
            target = k + v
            if target in mp:
                count += mp[target]
                if target == v:
                    count -= 1
            mp[v] -= 1

        return count
