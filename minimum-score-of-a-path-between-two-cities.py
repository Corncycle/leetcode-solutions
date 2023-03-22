from typing import List
from collections import defaultdict
import math

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for source, dest, length in roads:
            graph[source].append([dest, length])
            graph[dest].append([source, length])
        
        visited = set()
        frontier = [1]
        out = math.inf

        while frontier:
            curr = frontier.pop()
            visited.add(curr)
            for neigh, dist in graph[curr]:
                if neigh not in visited:
                    out = min(out, dist)
                    frontier.append(neigh)
        
        return out