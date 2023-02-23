from typing import List
import heapq

# this two-heap solution is due to the following youtube video:
# https://www.youtube.com/watch?v=1IUzNJ6TPEM

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfit = []
        minCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minCapital)

        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            w += -1 * heapq.heappop(maxProfit) if maxProfit else 0
        return w