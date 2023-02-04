from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1c = Counter(s1)
        for i in range(len(s2) - len(s1) + 1):
            if Counter(s2[i:i+len(s1)]) == s1c:
                return True
        return False