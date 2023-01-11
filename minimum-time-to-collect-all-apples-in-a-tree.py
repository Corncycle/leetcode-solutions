from typing import List
from collections import defaultdict, Counter

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph, incl = defaultdict(list), [False] * n
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def shouldBeIncluded(curr: int, parent: int):
            # a node should be included if either
            #   A) one of its children should be included (meaning it has a descendant with an apple)
            #   B) it has an apple itself
            incl[curr] = any([shouldBeIncluded(child, curr) for child in graph[curr] if child != parent]) or hasApple[curr]
            return incl[curr]
        shouldBeIncluded(0, -1)

        numIncl = Counter(incl)[True]
        return max(0, 2 * (numIncl - 1))