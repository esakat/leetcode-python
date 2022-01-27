#
# @lc app=leetcode id=286 lang=python3
#
# [286] Walls and Gates
#

# @lc code=start
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        for y, row in enumerate(rooms):
            for x, cell in enumerate(row):
                if cell == 0:
                    stack = []
                    if y > 0 and rooms[y-1][x] > 1:
                        rooms[y-1][x] = 1
                        stack.append([y-1, x])
                    if y < len(rooms)-1 and rooms[y+1][x] > 1:
                        rooms[y+1][x] = 1
                        stack.append([y+1, x])
                    if x > 0 and rooms[y][x-1] > 1:
                        rooms[y][x-1] = 1
                        stack.append([y, x-1])
                    if x < len(row)-1 and rooms[y][x+1] > 1:
                        rooms[y][x+1] = 1
                        stack.append([y, x+1])

                    while len(stack) > 0:
                        [i, j] = stack.pop()
                        now = rooms[i][j]
                        if i > 0 and rooms[i-1][j] > now+1:
                            rooms[i-1][j] = now+1
                            stack.append([i-1, j])
                        if i < len(rooms)-1 and rooms[i+1][j] > now+1:
                            rooms[i+1][j] = now+1
                            stack.append([i+1, j])
                        if j > 0 and rooms[i][j-1] > now+1:
                            rooms[i][j-1] = now+1
                            stack.append([i, j-1])
                        if j < len(row)-1 and rooms[i][j+1] > now+1:
                            rooms[i][j+1] = now+1
                            stack.append([i, j+1])                   
        
# @lc code=end

