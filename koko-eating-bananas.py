from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k: int) -> bool:
            return sum(ceil(p / k) for p in piles) <= h
        
        left, right = 1, max(piles)
        while left < right:
            mp = (left + right) // 2
            if canFinish(mp):
                right = mp
            else:
                left = mp + 1
        return left