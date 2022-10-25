from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        cleanWord1 = []
        cleanWord2 = []
        for word in word1:
            splitWord = [*word]
            for char in splitWord:
                cleanWord1.append(char)
        for word in word2:
            splitWord = [*word]
            for char in splitWord:
                cleanWord2.append(char)
        if len(cleanWord1) != len(cleanWord2):
            return False
        for i in range(len(cleanWord1)):
            if cleanWord1[i] != cleanWord2[i]:
                return False
        return True

# The easy solution is actually quite fast
'''class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)'''

# Traversing strings appears slower than using "".join(word)
'''class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        wordIndex1 = 0
        charIndex1 = 0
        wordIndex2 = 0
        charIndex2 = 0
        while wordIndex1 < len(word1) and wordIndex2 < len(word2):
            #print(f"comparing {word1[wordIndex1][charIndex1]} and {word2[wordIndex2][charIndex2]}")
            if word1[wordIndex1][charIndex1] != word2[wordIndex2][charIndex2]:
                return False
            else:
                wordIndex1, charIndex1 = self.nextIndex(word1, wordIndex1, charIndex1)
                #print(f"{wordIndex1}, {charIndex1}")
                wordIndex2, charIndex2 = self.nextIndex(word2, wordIndex2, charIndex2)
                #print(f"{wordIndex2}, {charIndex2}")
        return wordIndex1 >= len(word1) and wordIndex2 >= len(word2)

    def nextIndex(self, listOfStrings, wordIndex, charIndex):
        if charIndex + 1 >= len(listOfStrings[wordIndex]):
            return wordIndex + 1, 0
        else:
            return wordIndex, charIndex + 1'''
