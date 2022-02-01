#
# @lc app=leetcode id=1086 lang=python3
#
# [1086] High Five
#

# @lc code=start
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dct = dict()
        for score in items:
            if score[0] in dct:
                dct[score[0]].append(score[1])
            else:
                dct[score[0]] = [score[1]]

        ans = []
        for k, v in dct.items():
            v.sort()
            v.reverse()
            avg = 0
            num = min(5, len(v))
            for i in range(num):
                avg += v[i]
            avg = avg // num
            ans.append([k, avg])

        ans.sort()
        return ans


# @lc code=end

