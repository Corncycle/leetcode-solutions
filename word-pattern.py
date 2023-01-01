from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        spl = s.split()
        if len(spl) != len(pattern):
            return False
        matches = defaultdict(str)
        for patt, word in zip(pattern, s.split()):
            if not matches[patt]:
                matches[patt] = word
                continue
            if matches[patt] != word:
                return False
        return len(set(matches.values())) == len(matches)