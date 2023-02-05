from typing import List
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        out, pc, sc = [], Counter(p), Counter(s[:len(p)])
        if pc == sc:
            out.append(0)
        for i in range(1, len(s) - len(p) + 1):
            sc[s[i-1]] -= 1
            sc[s[i-1+len(p)]] += 1
            if sc == pc:
                out.append(i)
        return out