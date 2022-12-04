from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        leftSum = nums[0]
        rightSum = sum(nums) - nums[0]
        n = len(nums)
        absDiffs = [ abs(leftSum - rightSum // (n - 1)) ]
        for i in range(1, n - 1):
            leftSum += nums[i]
            rightSum -= nums[i]
            absDiffs.append(abs((leftSum // (i + 1)) - (rightSum // (n - i - 1))))
        leftSum += nums[n - 1]
        absDiffs.append(abs(leftSum // n))
        return absDiffs.index(min(absDiffs))