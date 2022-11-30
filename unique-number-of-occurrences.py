from typing import List
from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = defaultdict(int)
        for num in arr:
            occ[num] += 1
        metaOcc = defaultdict(int)
        print(occ)
        for num, val in occ.items():
            if metaOcc[val] > 0:
                return False
            metaOcc[val] += 1
        return True