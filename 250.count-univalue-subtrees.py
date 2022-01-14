#
# @lc app=leetcode id=250 lang=python3
#
# [250] Count Univalue Subtrees
#

from typing import Optional


# @lc code=start
from unittest import result


class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        result = 0
        END_LEAF = -1001
        NG = 1001
        
        def helper(now: Optional[TreeNode]) -> int:
            if now is None:
                return END_LEAF
            
            r = helper(now.right)
            l = helper(now.left)

            if (l == END_LEAF or l == now.val) and (r == END_LEAF or r == now.val):
                nonlocal result
                result += 1
                return now.val
            else:
                # 範囲外、NGの値を返す
                return NG

        helper(root)

        return result

# nonlocalの使い方に悩んだ
# https://qiita.com/domodomodomo/items/6df1419767e8acb99dd7
# 再帰で更新するのリストばっかりだった、intとかを更新するときは、nonlocal付けないとエラーになる（ローカル変数として扱われる）

# @lc code=end

