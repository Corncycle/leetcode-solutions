class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        tCount, fCount = 0, 0
        left, right = 0, 0
        best = 0

        while True:
            right += 1
            if answerKey[right-1] == "F":
                fCount += 1
            else:
                tCount += 1
            while fCount > k and tCount > k:
                left += 1
                if answerKey[left-1] == "F":
                    fCount -= 1
                else:
                    tCount -= 1
            best = max(best, tCount + fCount)
            if right == len(answerKey):
                break

        return best
