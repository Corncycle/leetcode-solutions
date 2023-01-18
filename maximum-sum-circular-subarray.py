from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        bestEndI, worstEndI = [nums[0]], [nums[0]]
        numsIter = iter(nums)
        next(numsIter)
        foundPos = nums[0] >= 0
        total = nums[0]
        for i, num in enumerate(numsIter):
            if num >= 0:
                foundPos = True
            bestEndI.append(max(num, num + bestEndI[-1]))
            worstEndI.append(min(num, num + worstEndI[-1]))
            total += num
        if not foundPos:
            return max(bestEndI)
        return max(max(bestEndI), total - min(worstEndI))