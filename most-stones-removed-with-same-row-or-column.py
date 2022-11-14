from typing import List

# Use BFS to determine connected components. All but one stone in each
# component can be removed from the board (you can prove that this can always
# be done by induction)
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        remainingStones = stones.copy()

        numComponents = 0
        while remainingStones:
            numComponents += 1
            frontier = [remainingStones.pop()]
            while frontier:
                current = frontier.pop()
                connectedToCurrent = [stone for stone in remainingStones if stone[0] == current[0] or stone[1] == current[1]]
                frontier.extend(connectedToCurrent)
                remainingStones = [stone for stone in remainingStones if stone not in connectedToCurrent]
        return len(stones) - numComponents