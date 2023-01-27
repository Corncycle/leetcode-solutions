from typing import List

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # sets have O(1) lookup compared to O(n) lookup for lists
        # can probably speed this up even further by caching isConcat calls 
        # but this suffices
        swords = set(words)
        def isConcat(word):
            for i in range(1, len(word)):
                if word[:i] in swords:
                    if word[i:] in swords or isConcat(word[i:]):
                        return True
            return False
        
        out = []
        for word in words:
            if isConcat(word):
                out.append(word)
        return out