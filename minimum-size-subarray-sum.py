from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        runningSum = 0
        best = len(nums)+1

        while True:
            right += 1
            runningSum += nums[right-1]
            while runningSum - nums[left] >= target:
                runningSum -= nums[left]
                left += 1
            if runningSum >= target:
                best = min(best, right - left)
            if right == len(nums):
                break

        return best if best <= len(nums) else 0