from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        placePointer = 0
        lookPointer = 0
        while lookPointer < len(nums):
            if nums[lookPointer] != nums[placePointer]:
                placePointer += 1
                nums[placePointer] = nums[lookPointer]
            lookPointer += 1
        while placePointer < len(nums) - 1:
            nums.pop(placePointer)