#
# @lc app=leetcode id=281 lang=python3
#
# [281] Zigzag Iterator
#

# @lc code=start
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.lnum = 2
        self.now = 0
        self.index = [0, 0]
        self.vec = [v1, v2]
        
        if len(v1) == 0:
            self.now = 1

    def next(self) -> int:
        if self.hasNext():
            ret = self.vec[self.now][self.index[self.now]]
            self.index[self.now] += 1
            for i in range(len(self.vec)):
                self.now += 1
                if self.now >= len(self.vec):
                    self.now = 0
                if self.index[self.now] < len(self.vec[self.now]):
                    break

            return ret
        else:
            return -1
            

    def hasNext(self) -> bool:
        return self.index[self.now] < len(self.vec[self.now])

# 普通の2pointerにした
# pointerをqueueで管理すると、k個のlistが来ても対処しやすい

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
# @lc code=end

