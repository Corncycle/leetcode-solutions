from typing import List
from heapq import heappop, heappush
import math

# this solution is due to timothy h chang
# https://www.youtube.com/watch?v=Yk0pKbQAw_w

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        richNums = []
        for num in nums:
            nMin, nMax = num, num
            while nMin % 2 == 0:
                nMin //= 2
            if nMax % 2 == 1:
                nMax *= 2
            heappush(richNums, (nMin, nMax))
        currMax = max(i for i, j in richNums)
        bestFound = math.inf
        while len(richNums) == len(nums):
            i, j = heappop(richNums)
            bestFound = min(bestFound, currMax - i)
            if i < j:
                heappush(richNums, (i * 2, j))
                currMax = max(currMax, i * 2)
        return bestFound