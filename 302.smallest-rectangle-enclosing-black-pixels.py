#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#

# @lc code=start
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        minx = sys.maxsize
        miny = sys.maxsize
        maxx = -sys.maxsize
        maxy = -sys.maxsize

        m = len(image)
        n = len(image[0])
        
        seen = [[False for i in range(n)] for j in range(m)]
        seen[x][y] = True
        stuck = [(x, y)]

        while len(stuck) > 0:
            (h, w) = stuck.pop()
            minx = min(minx, h)
            maxx = max(maxx, h)
            miny = min(miny, w)
            maxy = max(maxy, w)
            
            
            if h > 0 and image[h-1][w] == "1" and not seen[h-1][w]:
                seen[h-1][w] = True
                stuck.append((h-1, w))  
            if h < m-1 and image[h+1][w] == "1" and not seen[h+1][w]:
                seen[h+1][w] = True
                stuck.append((h+1, w))  
            if w > 0 and image[h][w-1] == "1" and not seen[h][w-1]:
                seen[h][w-1] = True
                stuck.append((h, w-1))  
            if w < n-1 and image[h][w+1] == "1" and not seen[h][w+1]:
                seen[h][w+1] = True
                stuck.append((h, w+1))

        
        
        return (maxx - minx + 1) * (maxy - miny + 1)


# 愚直なBFSアプローチ
# Time O(mn), Space O(mn)

# 最適解だと、列・行ごとに別々にやって、バイナリーサーチを組み合わせるらしい
# Time O(mlogn + nlogm) , Space O(1)になるらしい　すげ

# @lc code=end

