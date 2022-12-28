from typing import List
import heapq

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        for i in range(k):
            res = heapq.heappop(heap) // 2
            heapq.heappush(heap, res)
        return -sum(heap)