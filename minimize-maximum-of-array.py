from typing import List
from math import ceil

# this approach is given in the editorial for the problem:
# https://leetcode.com/problems/minimize-maximum-of-array/editorial/

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        partialAnswer = 0
        prefixSum = 0
        for i, num in enumerate(nums):
            prefixSum += num
            partialAnswer = max(partialAnswer, ceil(prefixSum / (i + 1)))
        return partialAnswer
