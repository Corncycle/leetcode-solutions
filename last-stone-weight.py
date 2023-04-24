from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-stone for stone in stones]
        heapify(s)
        
        while len(s) > 1:
            first, second = heappop(s), heappop(s)
            if first < second:
                heappush(s, first - second)
        
        return -s[0] if s else 0