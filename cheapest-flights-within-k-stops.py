from typing import List
from collections import defaultdict
import math

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(set)
        for s, d, price in flights:
            graph[s].add((d, price))
        bestFound = [math.inf] * n
        bestFound[src] = 0

        frontier = set([src])
        for _ in range(k+1):
            if not frontier:
                return -1 if bestFound[dst] == math.inf else bestFound[dst]
            newFrontier = set()
            pending = bestFound.copy()
            for source in frontier:
                neighs = graph[source]
                for neigh, price in neighs:
                    if bestFound[source] + price < pending[neigh]:
                        pending[neigh] = bestFound[source] + price
                        newFrontier.add(neigh)
            frontier = newFrontier
            bestFound = pending
        return -1 if bestFound[dst] == math.inf else bestFound[dst] 