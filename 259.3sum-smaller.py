#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#

from typing import List
import bisect


# @lc code=start
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        # まずソート
        nums.sort()

        result = 0

        # 条件が len(nums) < 3500なので10^3, ２重ループまではできる。
        # ソート済みなので、２重ループから、残りを２重ループ目移行で、2分探索すれば N^2logNでいけるはず
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                # 2分探索, lower_bound
                k = bisect.bisect_left(nums, target-(nums[i] + nums[j])) - 1
                if k > j:
                    result += k - j


        return result


# 回答見てtwo pointers使うやつ賢かった。
# 負の値もあるので、左から数えて1,2番目の間のインデックスが正しいよ
# def threeSumSmaller(self, nums, target):
#     nums.sort()
#     count = 0
#     for k in range(len(nums)):
#         i, j = 0, k - 1
#         while i < j:
#             if nums[i] + nums[j] + nums[k] < target:
#                 count += j - i
#                 i += 1
#             else:
#                 j -= 1
#     return count


# @lc code=end
