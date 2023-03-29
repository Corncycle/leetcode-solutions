from typing import List
from collections import deque

# nice rearrangement inequality problem
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if all(s <= 0 for s in satisfaction):
            return 0
        sats = deque(sorted(satisfaction))
        n = len(sats)
        negCount = sum(1 for s in sats if s < 0)
        maxFound = 0
        for _ in range(negCount + 1):
            likeSum = 0
            # can probably make this faster with clever partial sum trickery
            for i, val in enumerate(sats, start=1):
                likeSum += i * val
            maxFound = max(maxFound, likeSum)
            sats.popleft()
        return maxFound