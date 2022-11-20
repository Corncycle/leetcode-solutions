class Solution:
    def calculate(self, s: str) -> int:
        sAsList = []
        i = 0
        while i < len(s):
            if s[i] in "()+-":
                sAsList.append(s[i])
                i += 1
            elif s[i] in "1234567890":
                num = ""
                while i < len(s) and s[i] in "1234567890":
                    num += s[i]
                    i += 1
                sAsList.append(int(num))
            else:
                i += 1
        return(self.reduce(sAsList))

    def reduce(self, l: list) -> None:
        if ")" in l:
            start = l.index(")")
            i = start - 1
            while l[i] != "(":
                i -= 1
            parenReduced = self.reduce(l[i+1:start])
            del l[i:start+1]
            l.insert(i, parenReduced)
            return self.reduce(l)
        else:
            if l[0] == "-":
                l.insert(0, 0)
            total = l[0]
            i = 1
            while i < len(l):
                total = total + l[i + 1] if l[i] == "+" else total - l[i + 1]
                i += 2
            return total