class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        characterList = []
        backwardsPointer = len(s) - 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        for char in s:
            if char in vowels:
                while s[backwardsPointer] not in vowels:
                    backwardsPointer -= 1
                characterList.append(s[backwardsPointer])
                backwardsPointer -= 1
            else:
                characterList.append(char)
        return "".join(characterList)