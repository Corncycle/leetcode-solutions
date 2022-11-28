from typing import List
from collections import defaultdict

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = defaultdict(int)
        for match in matches:
            losses[match[0]] += 0
            losses[match[1]] += 1
        out = [sorted([p for p, numL in losses.items() if numL == 0]), 
            sorted([p for p, numL in losses.items() if numL == 1])]
        return out