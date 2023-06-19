from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        curr = 0    
        for diff in gain:
            curr += diff
            m = max(curr, m)
        return m