from typing import List
from queue import Queue

# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Space Complexity: O(N)
        #
        # que = Queue()
        # for i, v in enumerate(nums):
        #     if v != 0:
        #         que.put(i)
        #
        # for i, v in enumerate(nums):
        #     if que.empty():
        #         break
        #     index = que.get()
        #     if i != index:
        #         nums[i], nums[index] = nums[index], nums[i]

        # Space Complexity: O(1), but there is little waste
        #
        # lastNonZeroIndex = 0
        # for v in nums:
        #     if v != 0:
        #         nums[lastNonZeroIndex] = v
        #         lastNonZeroIndex += 1
        #
        # while lastNonZeroIndex < len(nums):
        #     nums[lastNonZeroIndex] = 0
        #     lastNonZeroIndex += 1

        # If you use swap, traverse count is only once.
        lastNonZeroIndex = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIndex], nums[i] = nums[i], nums[lastNonZeroIndex]
                lastNonZeroIndex += 1
