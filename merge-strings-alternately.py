class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        out = []
        while i < len(word1) and j < len(word2):
            if i == j:
                out.append(word1[i])
                i += 1
            else:
                out.append(word2[j])
                j += 1
        while i < len(word1):
            out.append(word1[i])
            i += 1
        while j < len(word2):
            out.append(word2[j])
            j += 1
        return "".join(out)