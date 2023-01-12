from typing import List
from collections import defaultdict

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph, counts = defaultdict(list), [0] * n
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        def trackSubTree(node: int, parent: int):
            children = [neighbor for neighbor in graph[node] if neighbor != parent]
            localCounts = defaultdict(int)
            localCounts[labels[node]] += 1
            for child in children:
                d = trackSubTree(child, node)
                for key, val in d.items():
                    localCounts[key] += val
            counts[node] = localCounts[labels[node]]
            return localCounts

        trackSubTree(0, None)
        return counts