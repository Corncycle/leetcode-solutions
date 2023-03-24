from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for s, d in connections:
            # "incorrectly" facing edge
            graph[s].append([d, 1])
            # "correctly" facing edge
            graph[d].append([s, 0])

        frontier = [0]
        visited = {0}
        count = 0
        while frontier:
            curr = frontier.pop()
            for neigh, weight in graph[curr]:
                if neigh not in visited:
                    frontier.append(neigh)
                    visited.add(neigh)
                    count += weight
        
        return count