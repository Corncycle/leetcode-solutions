from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        requiredJumps = 1 if len(nums) > 1 else 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= requiredJumps:
                requiredJumps = 0
            requiredJumps += 1
        return nums[0] >= requiredJumps