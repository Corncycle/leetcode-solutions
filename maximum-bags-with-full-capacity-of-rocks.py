from typing import List

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        needed = [cap - ro for cap, ro in zip(capacity, rocks)]
        needed.sort()
        i, remaining = 0, additionalRocks
        while i < len(needed) and remaining >= needed[i]:
            remaining -= needed[i]
            i += 1
        return i