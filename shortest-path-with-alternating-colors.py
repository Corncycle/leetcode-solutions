from typing import List
from collections import defaultdict

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        rgraph, bgraph = defaultdict(set), defaultdict(set)
        for s, d in redEdges:
            rgraph[s].add(d)
        for s, d in blueEdges:
            bgraph[s].add(d)
        
        # (v, c) in `visited` indicates we have been at vertex v, with next
        # step only permitted to move along a c-colored edge
        visited = set([(0, "r"), (0, "b")])
        frontier = set([(0, "r"), (0, "b")])
        newFrontier = set()
        depth = 1
        out = [-1] * n
        out[0] = 0
        while frontier:
            for v, c in frontier:
                if c == "r":
                    for dest in rgraph[v]:
                        if (dest, "b") not in visited:
                            visited.add((dest, "b"))
                            newFrontier.add((dest, "b"))
                            if out[dest] == -1:
                                out[dest] = depth
                else:
                    for dest in bgraph[v]:
                        if (dest, "r") not in visited:
                            visited.add((dest, "r"))
                            newFrontier.add((dest, "r"))
                            if out[dest] == -1:
                                out[dest] = depth
            depth += 1
            frontier = newFrontier
            newFrontier = set()
        return out