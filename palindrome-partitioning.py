from typing import List
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        out = []
        for i in range(1, len(s)):
            pref = s[:i]
            if self.isPalindrome(pref):
                rems = self.partition(s[i:])
                out += [[pref] + rem for rem in rems]
        if self.isPalindrome(s):
            out += [[s]]
        return out

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]