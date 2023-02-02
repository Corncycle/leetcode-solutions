from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            d[order[i]] = chr(i+97)
        
        def translate(s):
            out = []
            for char in s:
                out.append(d[char])
            return "".join(out)

        translated = [translate(word) for word in words]
        return all(translated[i] <= translated[i+1] for i in range(len(words)-1))