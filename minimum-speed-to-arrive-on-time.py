from typing import List
import math

class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def isValidSpeed(speed):
            time = 0
            for d in dist[:-1]:
                time += math.ceil(d / speed)
            time += dist[-1] / speed
            return time <= hour

        left, right = 1, 10 ** 7 # justification for right: dist[i] <= 10 ** 5, and hour has at most 2 digits after the decimal point

        while left < right:
            mid = (left + right) // 2
            if isValidSpeed(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if isValidSpeed(left) else -1