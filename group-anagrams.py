from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for str in strs:
            strSorted = "".join(sorted(str))
            if strSorted in found:
                found[strSorted].append(str)
            else:
                found[strSorted] = [str]
        return found.values()