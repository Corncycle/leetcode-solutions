from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def computePaths(prefix):
            if prefix[-1] == len(graph) - 1:
                paths.append(prefix)
                return
            for dest in graph[prefix[-1]]:
                computePaths(prefix + [dest])
        
        computePaths([0])
        return paths