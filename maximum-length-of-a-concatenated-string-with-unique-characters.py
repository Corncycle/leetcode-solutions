from typing import List, Set

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        strSet = []
        for s in arr:
            sAsSet = set(s)
            if (len(sAsSet) == len(s)):
                strSet.append(sAsSet)
        return len(self.maxLengthGiven(set(), strSet))

    def maxLengthGiven(self, stringSoFar: Set[str], remaining: List[Set[str]]):
        if not remaining:
            return stringSoFar
        # print("checking " + self.setToStr(stringSoFar) + " with options " + self.remainingToString(remaining))
        max = stringSoFar
        for s in remaining:
            if not s.issubset(max):
                if s.isdisjoint(stringSoFar):
                    extended = stringSoFar.union(s)
                    removed = remaining.copy()
                    removed.remove(s)
                    better = self.maxLengthGiven(extended, removed)
                    if len(better) > len(max):
                        max = better
        return max

    def remainingToString(self, remaining):
        out = "["
        for s in remaining:
            out += self.setToStr(s) + ", "
        return out[:-2] + "]"

    def setToStr(self, s):
        out = ""
        for c in s:
            out += c
        return out