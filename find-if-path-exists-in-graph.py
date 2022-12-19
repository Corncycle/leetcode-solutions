from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        frontier = [source]
        visited = [source]
        while frontier:
            newFrontier = []
            for node in frontier:
                for edge in edges:
                    if node in edge:
                        other = [n for n in edge if n != node][0]
                        if other == destination:
                            return True
                        if other not in visited and other not in newFrontier:
                            newFrontier.append(other)
                            visited.append(other)
            frontier = newFrontier
        return False