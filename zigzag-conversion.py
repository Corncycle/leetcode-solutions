# Logic was worked on paper with a few examples. The key idea is that the
# first and last rows must be handled differently from the middle rows

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s
        out, i, offset = [], 0, 2 * (numRows - 1)
        while i < len(s):
            out.append(s[i])
            i += offset
        for j in range(1, numRows - 1):
            i = j
            while i < len(s):
                out.append(s[i])
                if i + (offset - 2 * j) < len(s):
                    out.append(s[i + (offset - 2 * j)])
                i += offset
        i = numRows - 1
        while i < len(s):
            out.append(s[i])
            i += offset
        return "".join(out)