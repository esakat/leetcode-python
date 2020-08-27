from queue import *

class MovingAverage:


    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.sum = 0
        self.que = Queue()


    def next(self, val: int) -> float:
        if self.que.qsize() == self.size:
            v = self.que.get()
            self.sum -= v

        self.sum += val
        self.que.put(val)
        return self.sum / Queue.qsize(self.que)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)