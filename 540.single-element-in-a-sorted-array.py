#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1   
        # バイナリーサーチでいける
        # 1つだけユニークで残りは2つという条件の配列は必ず、奇数個の配列になる
        # ので、バイナリサーチで配列の中央の値をとる。
        # その値と同じやつが左右どちらにあるか調べる
        # 同じ値2つを取り出したときに残った左右の部分配列で奇数個の方を新しい探索対象とする
        while lo < hi:
            mid = lo + (hi - lo) // 2
            # 中央で分割した時に左右の部分配列が偶数個か奇数個かで判定条件が変わる
            halves_are_even = (hi - mid) % 2 == 0
            if nums[mid + 1] == nums[mid]:
                if halves_are_even:
                    lo = mid + 2
                else:
                    hi = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if halves_are_even:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                return nums[mid]
        return nums[lo]
        

# バイナリサーチの案は思いついたけど、分割した時の左右の偶数・奇数で判定するのが出てこずめんどくなって答え見ちゃった。
# バイナリサーチ特殊実装苦手だなぁ
        

# @lc code=end

