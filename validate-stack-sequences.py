from typing import List
from collections import deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque()
        pu, po = deque(pushed), deque(popped)

        while pu or po:
            if po:
                if stack and po[0] == stack[-1]:
                    stack.pop()
                    po.popleft()
                else:
                    if not pu:
                        return False
                    else:
                        stack.append(pu.popleft())
            else:
                stack.append(pu.popleft())

        return not pu and not po and not stack