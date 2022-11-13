class Solution:
    def reverseWords(self, s: str) -> str:
        wordsAsList = s.strip().split()
        wordsAsList.reverse()
        return " ".join(wordsAsList)