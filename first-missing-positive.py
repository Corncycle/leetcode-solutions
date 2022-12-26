from typing import List
from collections import defaultdict

# problem statement is very ambiguous. if nums.length is n, then this solution
# does not solve in O(1) space, but nums.length is bounded by the rather small
# 10 ** 5. all of the "O(1)" space solutions i have seen involve mutating the
# original array which i find hard to argue use O(1) space.
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lookup = defaultdict(int)
        for num in nums:
            lookup[num] += 1
        i = 1
        while i <= 10 ** 5 + 1:
            if lookup[i] == 0:
                return i
            i += 1
        return -1