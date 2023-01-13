from typing import List
from collections import defaultdict
import heapq

class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(1, len(parent)):
            graph[parent[i]].append(i)

        self.maxFound = 1
        def dfs(node):
            heights = []
            for child in graph[node]:
                ch = dfs(child)
                if s[child] != s[node]:
                    heights.append(ch)
            h = 0
            p = 1
            if len(heights) == 1:
                h = heights[0] + 1
                p = h + 1
            elif len(heights) > 1:
                h, h2 = heapq.nlargest(2, heights)
                h += 1
                p = h + h2 + 2
            self.maxFound = max(self.maxFound, p)
            return h
            
        dfs(0)
        return self.maxFound