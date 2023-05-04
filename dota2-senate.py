from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque([i for i in range(len(senate)) if senate[i] == "R"])
        d = deque([j for j in range(len(senate)) if senate[j] == "D"])

        while r and d:
            rfront = r.popleft()
            dfront = d.popleft()

            if rfront < dfront:
                r.append(rfront + len(senate))
            else:
                d.append(dfront + len(senate))

        return "Radiant" if r else "Dire"