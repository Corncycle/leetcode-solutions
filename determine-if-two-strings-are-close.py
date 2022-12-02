from string import ascii_lowercase

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        w1count, w2count = [], []
        w1dict, w2dict = set(), set()
        for char in ascii_lowercase:
            if char in word1:
                w1count.append(word1.count(char))
                w1dict.add(char)
            if char in word2:
                w2count.append(word2.count(char))
                w2dict.add(char)
        return w1dict == w2dict and sorted(w1count) == sorted(w2count)