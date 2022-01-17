#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#

from typing import List
import bisect


# @lc code=start
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = [[] for i in range(n)]
        for edge in edges:
            tree[edge[0]].append(edge[1])
            tree[edge[1]].append(edge[0])
        
        stack = []
        seen = [False for i in range(n)]
        seen[0] = True
        for v in tree[0]:
            stack.append([v, 0])

        while len(stack) > 0:
            [next, par] = stack.pop()
            seen[next] = True
            for v in tree[next]:
                if seen[v] and v != par:
                    return False
                if seen[v]:
                    continue
                stack.append([v, next])

        print("here")
        print(seen)

        valid = True
        for v in seen:
            valid = valid and v

        return valid

# Treeを実際に構築した後にBFSやる。
# BFSの条件でどの親から来たかを確認する。
# すでに見ている葉かつそれが親じゃなければ、循環してるのでNG
# また、edgeが途中で途切れて、一部辿り着けない葉というNGパターンもあるかもなので、最後にそれチェックしてる

# @lc code=end
