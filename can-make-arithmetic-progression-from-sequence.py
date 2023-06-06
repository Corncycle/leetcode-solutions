from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return True
        
        sarr = sorted(arr)
        d = sarr[0] - sarr[1]
        for i in range(1, len(sarr) - 1):
            if sarr[i] - sarr[i+1] != d:
                return False
        return True