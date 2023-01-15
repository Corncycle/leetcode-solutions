from typing import List
from collections import defaultdict
from math import comb

# this solution is heavily based on the solution given here:
# https://leetcode.com/problems/number-of-good-paths/solutions/3053513/python3-union-find-explained/
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        graph, nodesByVal = defaultdict(list), defaultdict(set)
        for i, v in enumerate(vals):
            nodesByVal[v].add(i)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)

        UF = {}
        def find(x):
            if x not in UF:
                UF[x] = x
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]
        def union(x, y):
            UF[find(x)] = find(y)

        out = len(vals)
        for val in sorted(nodesByVal):
            for node in nodesByVal[val]:
                for neigh in graph[node]:
                    if vals[neigh] <= val:
                        union(neigh, node)
            
            components = defaultdict(int)
            for node in nodesByVal[val]:
                components[find(node)] += 1
            
            for root in components.keys():
                out += comb(components[root], 2)
        return out