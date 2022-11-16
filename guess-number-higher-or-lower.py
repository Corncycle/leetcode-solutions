# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n
        while low < high:
            newGuess = (low + high) // 2
            guessOutput = guess(newGuess)
            if guessOutput == 1:
                low = newGuess + 1
            elif guessOutput == -1:
                high = newGuess
            else:
                return newGuess
        return low