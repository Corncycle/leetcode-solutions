from typing import List

# this bitwise approach is due to this solution
# https://leetcode.com/problems/single-number-ii/solutions/3714938/c-more-intuitive-bit-solution/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        out = 0
        for bit in range(0, 32):
            bitsum = 0
            for num in nums:
                bitsum += (num >> bit) & 1
            if bitsum % 3 != 0:
                if bit < 31:
                    out = out | (1 << bit)
                else:
                    out -= 1 << 31
        return out