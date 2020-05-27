from typing import List

# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        height = len(grid)
        if height == 0:
            return 0
        width = len(grid[0])
        if width == 0:
            return 0

        seen = [[-1] * width for i in range(height)]

        def dfs(h: int, w: int) -> int:
            nonlocal seen, grid, height, width
            ret = 1
            if h-1 >= 0 and seen[h-1][w] == -1 and grid[h-1][w] == 1:
                seen[h - 1][w] = 1
                ret += dfs(h-1, w)
            if h+1 < height and seen[h+1][w] == -1 and grid[h+1][w] == 1:
                seen[h + 1][w] = 1
                ret += dfs(h+1, w)
            if w-1 >= 0 and seen[h][w-1] == -1 and grid[h][w-1] == 1:
                seen[h][w - 1] = 1
                ret += dfs(h, w-1)
            if w+1 < width and seen[h][w+1] == -1 and grid[h][w+1] == 1:
                seen[h][w + 1] = 1
                ret += dfs(h, w+1)

            return ret

        max_area = 0
        for h, row in enumerate(grid):
            for w, v in enumerate(row):
                if seen[h][w] == -1 and grid[h][w] == 1:
                    seen[h][w] = 1
                    max_area = max(max_area, dfs(h, w))

        return max_area
