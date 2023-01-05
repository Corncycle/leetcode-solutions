from typing import List
from collections import deque

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        s = deque(sorted(points, key=lambda pair: pair[1]))
        lastArrow = s.popleft()[1]
        out = 1
        for balloon in s:
            if not balloon[0] <= lastArrow <= balloon[1]:
                lastArrow = balloon[1]
                out += 1
        return out