from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0 or newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        a, b = newInterval
        i = 0
        out = []
        while i < len(intervals) and a > intervals[i][1]:
            out.append(intervals[i])
            i += 1
        if i == len(intervals):
            out.append(newInterval)
            return
        left = min(a, intervals[i][0])
        last = None
        while i < len(intervals) and b >= intervals[i][0]:
            last = intervals[i]
            i += 1
        right = max(b, last[1]) if last else b
        out.append([left, right])
        while i < len(intervals):
            out.append(intervals[i])
            i += 1
        return out