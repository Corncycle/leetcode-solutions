from typing import List
from collections import defaultdict
from heapq import heappop, heappush

# classic djikstra problem

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        for i, edge in enumerate(edges):
            prob = succProb[i]
            g[edge[0]].append((edge[1], prob))
            g[edge[1]].append((edge[0], prob))

        cumProbs = [0 for _ in range(n)]
        cumProbs[start] = -1

        unvisited = [(-1, start)]

        while unvisited:
            currProb, curr = heappop(unvisited)
            if curr == end:
                return -currProb

            for neigh, prob in g[curr]:
                if prob * currProb < cumProbs[neigh]:
                    heappush(unvisited, (prob * currProb, neigh))
                    cumProbs[neigh] = prob * currProb

        return -cumProbs[end]