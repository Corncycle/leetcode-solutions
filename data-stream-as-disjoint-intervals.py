from typing import List
from bisect import insort

class SummaryRanges:

    def __init__(self):
        self.arr = []

    def addNum(self, value: int) -> None:
        if value not in self.arr:
            insort(self.arr, value)

    def getIntervals(self) -> List[List[int]]:
        out, i = [], 0
        left, last = self.arr[0], self.arr[0]
        while i < len(self.arr):
            if self.arr[i] > last + 1:
                out.append([left, last])
                left = self.arr[i]
            last = self.arr[i]
            i += 1
        out.append([left, last])
        return out