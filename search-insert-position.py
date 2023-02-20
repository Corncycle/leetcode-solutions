from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return 1 if target > nums[0] else 0
        while right - left > 1:
            if nums[left] > target:
                return left
            if nums[right] < target:
                return right + 1
            mp = (left + right) // 2
            if nums[mp] == target:
                return mp
            elif nums[mp] < target:
                left = mp
            else:
                right = mp
        if target <= nums[left]:
            return left
        elif target > nums[right]:
            return right + 1
        else:
            return right