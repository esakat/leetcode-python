from typing import List
from algorithm.unionfind import UnionFind

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for path in edges:
            uf.union(path[0], path[1])

        return uf.group_count()
