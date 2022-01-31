#
# @lc app=leetcode id=296 lang=python3
#
# [296] Best Meeting Point
#

# @lc code=start
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        # マトリックスをグラフにしてわーしゃるフロイド？
        # 制約的に厳しい　10^12になりそう
        # 友達の数(1の数)が少ないなら、各友達の点からBFSをして行って、合計値が一番小さいところにと思ったけどそれもむずい
        # 全マスが友達の可能性もある。
        # --- 思いついた　---
        # 列と行の個数と、どの列・行を選ぶのが最適かを決める
        countOfRow = [0] * len(grid)
        countOfColumn = [0] * len(grid[0])
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    countOfRow[i] += 1

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    countOfColumn[i] += 1

        bestRow = sys.maxsize
        bestColumn = sys.maxsize

        for i in range(len(grid)):
            tmp = 0
            for j in range(len(grid)):
                if i == j:
                    continue
                tmp += abs(i-j) * countOfRow[j]
            bestRow = min(bestRow, tmp)

        for i in range(len(grid[0])):
            tmp = 0
            for j in range(len(grid[0])):
                if i == j:
                    continue
                tmp += abs(i-j) * countOfColumn[j]
            bestColumn = min(bestColumn, tmp)

        return bestColumn + bestRow

        

# @lc code=end

