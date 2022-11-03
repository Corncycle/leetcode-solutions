from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        occurrences = {}
        count = 0
        for word in words:
            if word in occurrences:
                if word[0] == word[1]:
                    count += 4
                    occurrences[word] -= 1
                    if occurrences[word] == 0:
                        occurrences.pop(word)
                else:
                    occurrences[word] = occurrences[word] + 1
            else:
                reversed = word[1] + word[0]
                if reversed in occurrences:
                    count += 4
                    occurrences[reversed] -= 1
                    if occurrences[reversed] == 0:
                        occurrences.pop(reversed)
                else:
                    occurrences[word] = 1
                    
        for word in occurrences:
            if word[0] == word[1]:
                return count + 2
        return count