#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#

from audioop import reverse
from typing import List
import itertools


# @lc code=start
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        dct = dict()
        for v in s:
            if v in dct:
                dct[v] += 1
            else:
                dct[v] = 1
        
        # 回文チェック
        odd_count = 0
        for k, v in dct.items():
            if v % 2 == 1:
                odd_count += 1
                
        if (odd_count > 0 and len(s)%2 == 0) or odd_count > 1:
            return []

        ss = ""
        odd_s = ""
        for k, v in dct.items():
            if v > 1:
                tmp = k * (v//2)
                ss += tmp
            if v%2 == 1:
                odd_s = k

        s_lst = list(ss)
        s_lst.sort()
        result_set = set()
        for v in itertools.permutations(s_lst):
            rvss = reversed(v)
            result_set.add("".join(v) + odd_s + "".join(rvss))
        
        return list(result_set)
 
## 難しい。
## そのままやっちゃうと誓約がs < 16なので、16!全部チェックなので無理。
## まず文字が偶数回、奇数回それぞれどのくらい出るかを確認して、フィルタする
## フィルタ後は半分の文字列にする(偶数回は2で割ってあげて)-> aacc なら ac を作るみたいな
## この半分の文字列に対して順列を作る。すでにこの文字と同じ文字は同じ回数作れることが保証されてるので
## 順列 + "奇数回の文字" + reversed(順列)にすれば必ず回文になる
## これなら最大でも8!なので十分間に合う処理となる、一応set入れたり重複削除とかも必要かも(aaaaaaabbみたいな時対応)

# @lc code=end
