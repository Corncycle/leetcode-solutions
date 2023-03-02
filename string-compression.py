from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        compPtr, charPtr = 0, 0
        while charPtr < len(chars):
            currChar = chars[charPtr]
            count = 0
            while charPtr < len(chars) and chars[charPtr] == currChar:
                count += 1
                charPtr += 1
            chars[compPtr] = currChar
            compPtr += 1
            if count > 1:
                s = str(count)
                chars[compPtr:compPtr+len(s)] = list(s)
                compPtr += len(s)
        return compPtr