from typing import List

# https://leetcode.com/problems/number-of-islands/
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) is 0 or len(grid[0]) is 0:
            return 0

        h = len(grid)
        w = len(grid[0])

        group = [[-1] * w for i in range(h)]

        def dfs(y: int, x: int, g: int):
            nonlocal group, grid, h, w

            if y-1 >= 0 and group[y-1][x] == -1 and grid[y-1][x] == '1':
                group[y-1][x] = g
                dfs(y-1, x, g)
            if y+1 < h and group[y+1][x] == -1 and grid[y+1][x] == '1':
                group[y+1][x] = g
                dfs(y+1, x, g)
            if x-1 >= 0 and group[y][x-1] == -1 and grid[y][x-1] == '1':
                group[y][x-1] = g
                dfs(y, x-1, g)
            if x+1 < w and group[y][x+1] == -1 and grid[y][x+1] == '1':
                group[y][x+1] = g
                dfs(y, x+1, g)

        g = 0
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                if v == '1' and group[i][j] == -1:
                    group[i][j] = g
                    dfs(i, j, g)
                    g += 1

        return g
