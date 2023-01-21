from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def helper(s: str, remBreaks: int) -> List[str]:
            if s == "":
                return []
            if s[0] == "0":
                if remBreaks == 0:
                    return [["0"]] if len(s) == 1 else []
                return [["0"] + suffix for suffix in helper(s[1:], remBreaks - 1)]
            if remBreaks == 0:
                return [[s]] if 1 <= len(s) <= 3 and 0 < int(s) <= 255 else []
            out = []
            for i in range(1, min(len(s), 4)):
                prefix = s[:i]
                if s[i] == 0:
                    continue
                if int(s[0:i]) <= 255:
                    out += [[prefix] + suffix for suffix in helper(s[i:], remBreaks - 1)]
            return out
        return [".".join(arr) for arr in helper(s, 3)]