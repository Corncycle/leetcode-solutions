from typing import List

'''If k == 2 we can execute a bubble sort because sending either of the first
two characters to the end of the string, then rotating them back to the start
is equivalent to swapping them.

If k == 1 there are only k possible strings, and since k is specified to be 
less than 1000 we can afford to simply create all of them and compare them.
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        rotatedStrings = [s[i:] + s[0:i] for i in range(len(s))]
        return min(rotatedStrings)