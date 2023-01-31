from typing import List

# this solution uses the dp approach from the following video
# https://www.youtube.com/watch?v=7kURH3btcV4

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        scoreAge = [[0, 0]] + sorted([score, age] for score, age in zip(scores, ages))

        for i in range(1, len(scoreAge)):
            score, age = scoreAge[i]
            bestScore = -1
            for j in range(i):
                if scoreAge[j][1] <= age:
                    bestScore = max(bestScore, score + scoreAge[j][0])
            scoreAge[i][0] = bestScore
        
        return max(score for score, _ in scoreAge)