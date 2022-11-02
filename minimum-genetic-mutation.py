from typing import List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if start == end:
            return 0
        if end not in bank:
            return -1
        bank = set(bank)
        bank.add(end)
        numMutations = 0
        currentStrings = set()
        currentStrings.add(start)
        while currentStrings:
            bank = bank - currentStrings
            currentStrings = self.mutate(currentStrings, bank)
            numMutations += 1
            if end in currentStrings:
                return numMutations
        return -1
    
    def mutate(self, currentStrings, bank):
        newStrings = set()
        for bankString in bank:
            if self.listCanMutateInto(currentStrings, bankString):
                newStrings.add(bankString)
        return newStrings

    def listCanMutateInto(self, list, string):
        return any(self.isMutation(listString, string) for listString in list)

    def isMutation(self, string1, string2):
        if len(string1) != len(string2):
            return False
        foundDiff = False
        for i in range(len(string1)):
            if string1[i] != string2[i]:
                if not foundDiff:
                    foundDiff = True
                else:
                    return False
        return True