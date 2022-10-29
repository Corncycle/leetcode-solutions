from typing import List

''' Reasoning for this solution:
    Consider the problem in the case with 2 flowers. There is no reason to break up the planting
    of the flowers (why?), so there are only two possible choices, plant flower1 then plant
    flower2 or plant flower2 then plant flower1. Altogether, we can think of this as a single
    flower, with plant and grow time derived from the two flowers. The plant time is obviously
    p1 + p2, and the grow time is slightly more complicated, at g1 + max(0, g2 - p1 - g1),
    assuming flower1 has the faster grow time (draw some examples to see why). Then the algorithm
    is to combine pairs of flowers with the shortest grow times into single flowers until we are 
    left with one composite flower with the desired time.

    We manage our lists sorted from largest to smallest (reversed) because list.append(elm) 
    is much faster than list.insert(1, elm) for large lists, and we are frequently appending small
    values from the structure of the algorithm.
'''
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plantTime = [x for _, x in sorted(zip(growTime, plantTime), reverse=True)]
        growTime.sort(reverse=True)

        while len(plantTime) > 1:
            self.reduceProblem(plantTime, growTime)
        
        return plantTime[0] + growTime[0]

    def reduceProblem(self, plantTime: List[int], growTime: List[int]) -> None:
        l = len(plantTime) - 1
        newPlantTime = plantTime[l] + plantTime[l - 1]
        newGrowTime = growTime[l] + max(0, growTime[l - 1] - plantTime[l] - growTime[l])
        del plantTime[-2:]
        del growTime[-2:]
        i = l - 2

        while i >= 0:
            if newGrowTime <= growTime[i]:
                if i == l - 2:
                    growTime.append(newGrowTime)
                    plantTime.append(newPlantTime)
                    return
                growTime.insert(i, newGrowTime)
                plantTime.insert(i, newPlantTime)
                return
            i -= 1
        growTime.append(newGrowTime)
        plantTime.append(newPlantTime)