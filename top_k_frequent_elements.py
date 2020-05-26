from typing import List

# https://leetcode.com/problems/top-k-frequent-elements/
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for v in nums:
            if v in mp:
                mp[v] += 1
            else:
                mp[v] = 1

        sorted_mp = sorted(mp.items(), reverse=True, key=lambda x:x[1])
        n = 0
        lst = []
        for key, val in sorted_mp:
            if n >= k:
                break
            lst.append(key)
            n += 1

        return lst
