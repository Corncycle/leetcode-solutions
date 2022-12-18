from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) > 1:
            while tokens[i] not in ["+", "-", "*", "/"]:
                i += 1
            arg1 = int(tokens[i - 2])
            arg2 = int(tokens[i - 1])
            op = tokens[i]
            i -= 2
            for _ in range(3):
                tokens.pop(i)
            if op == "+":
                result = arg1 + arg2
            elif op == "-":
                result = arg1 - arg2
            elif op == "*":
                result = arg1 * arg2
            elif op == "/":
                result = arg1 // arg2
                if arg1 * arg2 < 0 and arg1 % arg2 != 0:
                    result += 1
            tokens.insert(i, result)
        return int(tokens[0])

s = Solution()
s.evalRPN(["4","-2","/","2","-3","-","-"])

print(4 % -2)