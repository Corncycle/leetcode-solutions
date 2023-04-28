from typing import List

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def areEquiv(a, b):
            diffs = sum((1 if ca != cb else 0) for ca, cb in zip(a, b))
            return diffs == 2 or diffs == 0
        groups = []
        while strs:
            frontier = [strs.pop()]
            groups.append([frontier[0]])
            while frontier:
                curr = frontier.pop()
                equivs = [s for s in strs if areEquiv(curr, s)]
                strs = [s for s in strs if s not in equivs]
                groups[-1].extend(equivs)
                frontier.extend(equivs)
        return len(groups)