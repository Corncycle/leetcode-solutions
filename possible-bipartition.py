from typing import List
from collections import defaultdict, deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        if n <= 2:
            return True
        edges = defaultdict(list)
        for dis in dislikes:
            edges[dis[0]].append(dis[1])
            edges[dis[1]].append(dis[0])
        
        visited = []
        colors = defaultdict(int)
        i = 1
        while len(visited) < n:
            while i in visited:
                i += 1
            frontier = deque([i])
            colors[i] = -1
            while frontier:
                person = frontier.popleft()
                visited.append(person)
                for neigh in edges[person]:
                    if neigh not in visited and neigh not in frontier:
                        frontier.append(neigh)
                    if colors[neigh] == colors[person]:
                        return False
                    colors[neigh] = -1 * colors[person]
        return True