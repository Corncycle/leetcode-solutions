from typing import List

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = [{} for num in nums]

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i]-nums[j] in dp[j]:
                    if nums[i]-nums[j] in dp[i]:
                        dp[i][nums[i]-nums[j]] = max(dp[i][nums[i]-nums[j]], dp[j][nums[i]-nums[j]]+1)
                    else:
                        dp[i][nums[i]-nums[j]] = dp[j][nums[i]-nums[j]]+1
                else:
                    dp[i][nums[i]-nums[j]] = 2

        return max(max(dic.values()) for dic in dp[1:])