from typing import List

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        t = sorted(nums)
        out = 0
        i, j = 0, 0
        while j < len(t) and t[i] == t[j]:
            j += 1
        while j < len(t):
            if t[j] > t[i]:
                out += 1
                i += 1
            j += 1
        return out