from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2) or set(s1) != set(s2):
            return False
        if len(s1) <= 1:
            return True
        elif len(s1) == 2:
            return s1 == s2 or s1 == s2[::-1]
        for i in range(1, len(s1)):
            if set(s1[:i]) == set(s2[:i]) and set(s1[i:]) == set(s2[i:]):
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                    return True
            if set(s1[:i]) == set(s2[-i:]) and set(s1[i:]) == set(s2[:-i]):
                if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                    return True
        return False