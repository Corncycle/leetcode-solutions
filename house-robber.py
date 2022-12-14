from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        dp = [nums[0], nums[1], nums[0] + nums[2]]
        for i in range(3, len(nums)):
            dp.append(nums[i] + max(dp[i - 2], dp[i - 3]))
        return max(dp)