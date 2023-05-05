class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVowel(c):
            return c in ["a", "e", "i", "o", "u"]
        
        curr = 0
        for c in s[0:k]:
            if isVowel(c):
                curr += 1

        best = curr
        for i in range(1, len(s)-k+1):
            if isVowel(s[i-1]):
                curr -= 1
            if isVowel(s[i+k-1]):
                curr += 1
            best = max(best, curr)

        return best
