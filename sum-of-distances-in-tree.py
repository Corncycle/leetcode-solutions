from typing import List
from collections import defaultdict, deque

'''This solution is based on the explanation given by Timothy H Chang:
https://www.youtube.com/watch?v=OCGPug-KirQ

However, I use bfs instead of dfs to compute the outputs
'''
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.edges = defaultdict(list)
        for edge in edges:
            self.edges[edge[0]].append(edge[1])
            self.edges[edge[1]].append(edge[0])
        
        def populateDesc(node, par):
            if len(self.edges[node]) == 1 and par:
                self.desc[node] = 1
                return 1
            out = 0
            for n in self.edges[node]:
                if n != par:
                    out += populateDesc(n, node)
            self.desc[node] = 1 + out
            return 1 + out

        self.desc = {}
        populateDesc(0, None)

        def bfsGenerator():
            frontier = deque([(child, 0, 1) for child in self.edges[0]])
            while frontier:
                item = frontier.popleft()
                yield item
                node, par, d = item
                for child in self.edges[node]:
                    if child != par:
                        frontier.append((child, node, d + 1))

        dist = [0] * n
        # compute the sum of distances for the 0 node explicitly
        for item in bfsGenerator():
            _, __, d = item
            dist[0] += d
        # for all descendants, compute the sum of distances based on parent
        for item in bfsGenerator():
            node, par, _ = item
            dist[node] = dist[par] + n - 2 * self.desc[node]

        return dist