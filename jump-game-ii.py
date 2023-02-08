from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[-1] = 0
        for i in reversed(range(len(nums)-1)):
            if nums[i] > 0:
                nums[i] = min(1+nums[j] for j in range(i+1, min(i+1+nums[i], len(nums))))
            else:
                nums[i] = 1000000
        return nums[0]