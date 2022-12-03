# python's built-ins are awesome for this kind of problem
class Solution:
    def frequencySort(self, s: str) -> str:
        runs = [char * s.count(char) for char in set(s)]
        runs.sort(key=len, reverse=True)
        return "".join(runs)