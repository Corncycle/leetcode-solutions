class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        pa, pb, pc = a, b, c
        out = 0
        while pa or pb or pc:
            curr = pc % 2
            if curr == 1:
                if pa % 2 == 0 and pb % 2 == 0:
                    out += 1
            else:
                out += (pa % 2) + (pb % 2)
            pa = pa // 2
            pb = pb // 2
            pc = pc // 2
        return out