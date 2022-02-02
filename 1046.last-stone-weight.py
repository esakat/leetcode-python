#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        revstones = list(map(lambda x: x*(-1), stones))
        heapq.heapify(revstones)
        while len(revstones) > 0:
            y = heapq.heappop(revstones)
            y *= -1
            if len(revstones) == 0:
                return y
            x = heapq.heappop(revstones)
            x *= -1

            if y != x:
                y -= x
                heapq.heappush(revstones, y*(-1))
        
        return 0


# @lc code=end

