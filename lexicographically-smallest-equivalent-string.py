class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        UF = {}
        def find(x):
            if x not in UF:
                UF[x] = x
            curr = x
            while curr != UF[curr]:
                curr = UF[curr]
            return curr
    
        def union(x, y):
            rx, ry = find(x), find(y)
            rmin, rmax = min(rx, ry), max(rx, ry)
            UF[rmax] = rmin

        for c1, c2 in zip(s1, s2):
            union(c1, c2)

        out = [find(c) for c in baseStr]
        return "".join(out)