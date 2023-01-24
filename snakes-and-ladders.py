from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        brd = []
        # organize input into a reasonable 1-d list
        for i, row in enumerate(reversed(board)):
            if i % 2 == 1:
                row.reverse()
            brd.extend(row)
        # 0-index input
        brd = [x-1 if x > -1 else x for x in brd]
        frontier, visited, round = set([0]), set([0]), 0
        while frontier:
            if len(brd)-1 in frontier:
                return round
            newFrontier = set()
            for spot in frontier:
                for j in range(1, 7):
                    if spot + j < len(brd):
                        dest = spot + j if brd[spot + j] == -1 else brd[spot + j]
                        if dest not in visited and dest < len(brd):
                            newFrontier.add(dest)
                            visited.add(dest)
            frontier = newFrontier
            round += 1
        return -1