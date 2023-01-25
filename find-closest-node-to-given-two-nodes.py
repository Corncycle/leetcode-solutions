from typing import List
import math

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(start):
            depth, dists = 1, [math.inf] * len(edges)
            dists[start] = 0
            frontier, visited = set([start]), set([start])
            while frontier:
                newFrontier = set()
                for loc in frontier:
                    if edges[loc] >= 0 and edges[loc] not in visited:
                        dists[edges[loc]] = depth
                        newFrontier.add(edges[loc])
                        visited.add(edges[loc])
                frontier = newFrontier
                depth += 1
            return dists

        dists1 = bfs(node1)
        dists2 = bfs(node2)
        bestFound, foundAt = math.inf, -1
        for i in range(len(dists1)):
            if max(dists1[i], dists2[i]) < bestFound:
                bestFound = max(dists1[i], dists2[i])
                foundAt = i
        return foundAt