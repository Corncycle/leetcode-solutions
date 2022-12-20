from typing import List

# bog standard bfs
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]
        frontier = [0]
        while frontier:
            newFrontier = []
            for room in frontier:
                neighbors = rooms[room]
                for neigh in neighbors:
                    if neigh not in visited and neigh not in newFrontier:
                        visited.append(neigh)
                        newFrontier.append(neigh)
            frontier = newFrontier
        return len(visited) == len(rooms)