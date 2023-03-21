from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        zstart = 0
        out = 0
        while i < len(nums):
            if nums[i] != 0:
                if i > zstart:
                    diff = i - zstart
                    out += diff * (diff + 1) // 2
                zstart = i + 1
            i += 1
        if i > zstart:
            diff = i - zstart
            out += diff * (diff + 1) // 2
        return out