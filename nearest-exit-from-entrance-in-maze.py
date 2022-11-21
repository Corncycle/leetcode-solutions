from typing import List

class Solution:
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        start = (entrance[0], entrance[1])
        frontier = {start}
        depth = 0
        while frontier:
            depth += 1
            newFrontier = set()
            for location in frontier:
                maze[location[0]][location[1]] = "+"
                validNeighbors = set()
                for direction in self.directions:
                    neighbor = (location[0] + direction[0], location[1] + direction[1])
                    if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]):
                        if maze[neighbor[0]][neighbor[1]] == ".":
                            validNeighbors.add(neighbor)
                for neighbor in validNeighbors:
                    if neighbor[0] == 0 or neighbor[1] == 0 or neighbor[0] == len(maze) - 1 or neighbor[1] == len(maze[0]) - 1:
                        return depth
                newFrontier = newFrontier.union(validNeighbors)
            frontier = newFrontier
        return -1