from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        out = 0
        for i in range(len(strs[0])):
            if any(ord(strs[j][i]) > ord(strs[j+1][i]) for j in range(len(strs) - 1)):
                out += 1
        return out