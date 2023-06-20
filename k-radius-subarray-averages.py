from typing import List

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        out = [-1 for num in nums]
        if 2*k+1 > len(nums):
            return out
        
        partial = sum(nums[0:2*k+1])
        out[k] = partial // (2*k+1)
        for i in range(k+1, len(nums)-k):
            partial -= nums[i-k-1]
            partial += nums[i+k]
            out[i] = partial // (2*k+1)
        
        return out