from typing import List
from collections import defaultdict

'''I found this elegant dp solution on Timothy H Chang's youtube channel
(https://www.youtube.com/watch?v=EDHbVuHWljs). Although he credits someone else
for the approach, he does not give their name. I have written some comments
below that helped me understand the algorithm as I was trying to wrap my head
around it through some examples I did on paper.
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][diff] stores the number of ways to begin at index i and go back
        # by diff repeatedly while staying in the array
        # eg. if nums == [4, 5, 5, 6], i == 3, diff == 1, then dp[i][diff] == 4
        # because the ways to begin at nums[i] == 6 and go back by diff == 1
        # repeatedly while remaining in nums are the following 4 sequences:
        # 6 -> 5, 6 -> 5, 6 -> 5 -> 4, 6 -> 5 -> 4
        dp = [defaultdict(int) for _ in nums]
        out = 0
        for i in range(n):
            for j in range(i):
                diff = nums[j] - nums[i]
                dp[i][diff] += 1 + dp[j][diff]
                # the way we ensure that we only count sequences of length 3 or
                # longer is by incrementing out here by dp[j][diff] instead of
                # something related to dp[i][diff]. this way, a value in
                # dp[j][diff] only contributes to out if was already a nonzero
                # value, and then a larger i was found that continued the
                # arithmetic progression (hence the difference was found twice,
                # implying the progression is at least 3 long)
                out += dp[j][diff]
        return out