from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pque = []
        self.k = k
        heapq.heapify(self.pque)
        for v in nums:
            if len(self.pque) < k:
                heapq.heappush(self.pque, v)
            elif self.pque[0] <= v:
                heapq.heappush(self.pque, v)
                if len(self.pque) > k:
                    heapq.heappop(self.pque)

    def add(self, val: int) -> int:
        if len(self.pque) < self.k:
            heapq.heappush(self.pque, val)
        elif self.pque[0] <= val:
            heapq.heappush(self.pque, val)
            if len(self.pque) > self.k:
                heapq.heappop(self.pque)
        return self.pque[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)