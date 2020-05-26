from typing import List
import heapq

# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if k == 0 or len(nums1) == 0 or len(nums2):
            return []

        que = []
        heapq.heapify(que)
        heapq.heappush(que, (nums1[0]+nums2[0], 0, 0))

        used = set()
        ret = []
        while len(ret) < k:
            top = heapq.heappop(que)
            if top in used:
                continue
            else:
                used.add(top)

            index1 = top[1]
            index2 = top[2]
            ret.append([nums1[index1], nums2[index2]])
            if index1+1 >= len(nums1) and index2+1 >= len(nums2):
                break
            if index1 + 1 < len(nums1):
                heapq.heappush(que, (nums1[index1+1] + nums2[index2], index1+1, index2))
            if index2 + 1 < len(nums2):
                heapq.heappush(que, (nums1[index1] + nums2[index2+1], index1, index2+1))

        return ret
