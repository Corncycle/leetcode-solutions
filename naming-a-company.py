from typing import List
from collections import defaultdict

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        suffByPref = defaultdict(set)
        for idea in ideas:
            suffByPref[idea[0]].add(idea[1:])
        out = 0
        for p1 in suffByPref:
            for p2 in suffByPref:
                if p1 < p2:
                    s1 = suffByPref[p1] - suffByPref[p2]
                    s2 = suffByPref[p2] - suffByPref[p1]
                    out += len(s1) * len(s2)
        return out * 2