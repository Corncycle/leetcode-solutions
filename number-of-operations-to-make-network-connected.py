from typing import List
from collections import defaultdict

# the graph can be made connected if there are at least n-1 edges
# if so, then this will require m-1 adjustments, where m is the number of
# connected components in the graph
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        
        graph = defaultdict(list)
        for s, d in connections:
            graph[s].append(d)
            graph[d].append(s)

        nodes = set(range(n))
        components = []
        while nodes:
            frontier = [nodes.pop()]
            visited = set(frontier)
            while frontier:
                curr = frontier.pop()
                for neigh in graph[curr]:
                    if neigh not in visited:
                        nodes.remove(neigh)
                        frontier.append(neigh)
                        visited.add(neigh)
            components.append(visited)
        return len(components) - 1