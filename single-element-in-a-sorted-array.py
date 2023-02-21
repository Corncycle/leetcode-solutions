from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left != right:
            mp = (left + right) // 2
            if nums[mp-1] != nums[mp] and nums[mp+1] != nums[mp]:
                return nums[mp]
            if ((right - left) // 2) % 2 == 0:
                if nums[mp+1] == nums[mp]:
                    left = mp + 2
                else:
                    right = mp - 2
            else:
                if nums[mp+1] == nums[mp]:
                    right = mp - 1
                else:
                    left = mp + 1
        return nums[left]