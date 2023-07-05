from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        runs = []

        while i < len(nums):
            if nums[i] == 1:
                currRun = 0
                while i < len(nums) and nums[i] == 1:
                    currRun += 1
                    i += 1
                runs.append(currRun)
            else:
                i += 1
                while i < len(nums) and nums[i] != 1:
                    runs.append(0)
                    i += 1
        if len(runs) == 1:
            return runs[0] if (nums[0] != 1 or nums[1] != 1) else runs[0]-1
        else:
            return max(runs[i-1]+runs[i] for i in range(1, len(runs)))