from typing import List
from collections import defaultdict
from math import ceil

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(set)
        for s, d in roads:
            graph[s].add(d)
            graph[d].add(s)

        self.out = 0
        # doDesc returns the number of descendants of node i, assuming 0 is
        # the root of the tree
        def doDesc(i: int, parent: int) -> int:
            count = 0
            for child in graph[i]:
                if child != parent:
                    count += doDesc(child, i) + 1
            if i != 0:
                self.out += ceil((count + 1) / seats)
            return count
        doDesc(0, -1)
        return self.out