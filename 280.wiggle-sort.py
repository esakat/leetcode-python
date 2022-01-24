#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()


        # for i in range(1, len(nums), 2):
        #     if i >= len(nums) - 1:
        #         break
        #     nums[i], nums[i+1] = nums[i+1], nums[i]
        # 上自分で考えた回答　O (NlogN）

        # ワンパスで行ける方法
        for i in range(len(nums)-1):
            if (i % 2 == 0) == (nums[i] > nums[i+1]):
                nums[i], nums[i+1] = nums[i+1], nums[i]
        
# @lc code=end

