from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        diffs = 0
        i = 0
        while diffs < 3 and i < len(s):
            if s[i] != goal[i]:
                diffs += 1
            i += 1
        c = Counter(s)
        d = Counter(goal)
        if not c == d:
            return False
        if diffs > 2:
            return False
        elif diffs == 2:
            return True
        elif diffs == 1:
            return False
        else:
            return c.most_common()[0][1] > 1