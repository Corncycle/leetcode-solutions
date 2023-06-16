from typing import List
from math import comb

# this approach is due to the editorial for the problem
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/editorial/

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def dfs(nums: List[int]):
            if len(nums) <= 1:
                return 1
            head = nums[0]
            left = [n for n in nums if n < head]
            right = [n for n in nums if n > head]
            return comb(len(nums)-1, len(left)) * dfs(left) * dfs(right)
        
        return (dfs(nums) - 1) % (10 ** 9 + 7)