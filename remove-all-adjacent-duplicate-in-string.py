from collections import deque

class Solution:
    # The naive approach works fine
    def removeDuplicates(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = max(0, i-1)
            else:
                i += 1
        return s

    # A better stack approach by Leetcode user md2030
    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/solutions/2798052/python3-stack-approach-o-n-candy-crush/
    '''def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)'''