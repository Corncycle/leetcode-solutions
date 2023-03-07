from typing import List
from math import floor

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left = floor(totalTrips * min(time) / len(time))
        right = totalTrips * max(time)

        while left <= right:
            reached = 0
            mp = (left + right) // 2
            for t in time:
                reached += mp // t
            if reached < totalTrips:
                left = mp + 1
            else:
                right = mp - 1
        return left