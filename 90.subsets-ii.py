#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#

import copy
from typing import List

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        # if currentSubset in resを使わない版
        # 無駄な計算が減ってるはずなので速いはず

        res = []
        nums = sorted(nums)

        def backtracking(index: int, currentSubset: List[int]):
            res.append(currentSubset[:])

            for i in range(index, len(nums)):
                # ソート済みで、隣り合うのが同じ数の場合は重複するので、飛ばす
                if i > index and nums[i] == nums[i - 1]:
                    continue

                # ※
                currentSubset.append(nums[i])
                backtracking(i + 1, currentSubset)
                # 次のループでは、次の要素から開始とするsubsetを探すので除外する
                # 再帰の中でもやってるので、参照渡しでリスト渡していっても、※で追加された処理が削除されるのは変わりない
                currentSubset.pop()
        
        backtracking(0, [])
        return res


        
# @lc code=end

