from typing import List
from graph.unionfind import UnionFind

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for path in edges:
            uf.union(path[0], path[1])

        return uf.group_count()
