#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#



# @lc code=start
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # [[start1, end1], [start2, end2]...]

        def reverse(start: int, end: int):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        # once s reverse all
        # after this, sets of str will be placed correct pos, but each str is reversed.
        reverse(0, len(s)-1)


        # so after that, we will reverse all str sets.
        from_pos = 0
        for i in range(len(s)):
            if s[i] == " ":
                reverse(from_pos, i-1)
                from_pos = i + 1

        # last str sets not end with " ".
        # so we need do again
        reverse(from_pos, len(s)-1)


# どうやら最適解だった。時間かかったけど思いついてよかった。
# こういうのは慣れなのかな..?
        
# @lc code=end

