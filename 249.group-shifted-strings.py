#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#

from typing import List


# @lc code=start
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        tempDict = dict()
        for i, s in enumerate(strings):
            sl = list(s)
            firstletter = sl[0]
            distanceList = []
            for j, c in enumerate(sl):
                # ord使うとUNICODE整数値がわかる
                distance = ord(c) - ord(firstletter)
                if distance < 0:
                    distance += 26
                distanceList.append(str(distance))
            lastStr = ','.join(distanceList)
            if lastStr in tempDict:
                tempDict[lastStr].append(s)
            else:
                tempDict[lastStr] = [s]

        ans = []
        for v in tempDict.values():
            ans.append(v)

        return ans

# ちょっと富豪的すぎるかもだけど、できる
# 各文字の先頭文字を基準に、文字全体のそこからの距離を計算する
# 例: abc -> [0, 1, 2] ,, azd -> [0, 25, 3]みたいな
# その後このリストを,で結合して文字列にする[0, 25, 3] -> "0,25,3"みたいな、後でグループ化するのにはハッシュ使いたい。リストはハッシュアブルなオブジェクトじゃないため文字列型にする
# あとはこの文字列をキーに、値としては配列で元の文字列を入れていけば、グループ化が行える

# @lc code=end

