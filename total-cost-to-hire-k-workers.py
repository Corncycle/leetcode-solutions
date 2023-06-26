from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lpointer = candidates
        rpointer = max(candidates, len(costs)-candidates)-1

        lworkers = costs[:lpointer]
        rworkers = costs[rpointer+1:]
        
        heapify(lworkers)
        heapify(rworkers)

        total = 0

        for _ in range(k):
            # append the leftmost smallest cost to total
            if lworkers:
                if rworkers:
                    if lworkers[0] <= rworkers[0]:
                        total += heappop(lworkers)
                    else:
                        total += heappop(rworkers)
                else:
                    total += heappop(lworkers)
            else:
                total += heappop(rworkers)
                
            # push next worker to lworkers or rworkers if not all workers have been pushed
            if rpointer >= lpointer:
                if len(lworkers) < len(rworkers):
                    heappush(lworkers, costs[lpointer])
                    lpointer += 1
                else:
                    heappush(rworkers, costs[rpointer])
                    rpointer -= 1
        
        return total