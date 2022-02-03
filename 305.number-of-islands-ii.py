#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#

# @lc code=start
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = [[0 for i in range(m)] for j in range(n) ]
        now = 1
        ans = []
        for pos in positions:
            [y, x] = pos
            if grid[y][x] > 0:
                ans.append(ans[len(ans)-1])
                continue
            if 
        # union find じゃないと無理
        # 111
        # 0x0
        # 222
        # 上のような時にxを塗ると１、２の島を合併させないといけないので
        
# @lc code=end

