from collections import deque
import bisect

class MedianFinder:
    def __init__(self):
        self.lowerDeque = deque()
        self.upperDeque = deque()

    def addNum(self, num: int) -> None:
        if len(self.lowerDeque) == 0:
            self.lowerDeque.append(num)
            return
        if num <= self.lowerDeque[-1]:
            bisect.insort(self.lowerDeque, num)
        else:
            bisect.insort(self.upperDeque, num)
        self.balanceDeques()

    def findMedian(self) -> float:
        if len(self.lowerDeque) == len(self.upperDeque):
            return (self.lowerDeque[-1] + self.upperDeque[0]) / 2
        else:
            return self.lowerDeque[-1]

    def balanceDeques(self) -> None:
        if len(self.upperDeque) > len(self.lowerDeque):
            self.lowerDeque.append(self.upperDeque.popleft())
        elif len(self.lowerDeque) > len(self.upperDeque) + 1:
            self.upperDeque.appendleft(self.lowerDeque.pop())