from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        size = len(nums)
        sumsStartingFromZero = {}
        runningSum = 0
        for i in range(size):
            runningSum += nums[i]
            runningSum = runningSum % k
            if runningSum == 0 and i > 0:
                return True
            if runningSum in sumsStartingFromZero:
                # use -1 to indicate that the runningSum has been found twice
                # this is the max # of times the sum can be found without success
                if sumsStartingFromZero[runningSum] == -1:
                    return True
                if i - sumsStartingFromZero[runningSum] > 1:
                    return True
                sumsStartingFromZero[runningSum] = -1
            else:
                sumsStartingFromZero[runningSum] = i
        return False