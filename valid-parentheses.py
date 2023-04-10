from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        d = deque()
        while i < len(s):
            if s[i] in ["(", "[", "{"]:
                d.append(s[i])
            else:
                if not d:
                    return False
                op = d.pop()
                if op + s[i] not in ["()", "[]", "{}"]:
                    return False
            i += 1
        return not d