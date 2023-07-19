from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval : interval[1])
        end = -10000000
        count = len(intervals)
        for interval in intervals:
            if interval[0] >= end:
                count -= 1
                end = interval[1]
        return count