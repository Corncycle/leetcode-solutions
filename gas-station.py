from typing import List
from itertools import accumulate

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diffs = [g - c for g, c in zip(gas, cost)]
        accum = list(accumulate(diffs))
        if accum[-1] < 0:
            return -1
        else:
            return (accum.index(min(accum)) + 1) % len(accum)