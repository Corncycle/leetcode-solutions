from typing import List

'''I learned this approach of using a monotonic stack to better keep track
of left and right bounds for a given element from the youtube channel Got Up
Late. My slower implementation is commented below.

https://www.youtube.com/watch?v=KkfswNp44nk
'''
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        arr = [0] + arr + [0]
        total = 0
        for i, n in enumerate(arr):
            while stack and n < arr[stack[-1]]:
                p = stack.pop()
                total += arr[p] * (p - stack[-1]) * (i - p)
            stack.append(i)
        return total % (10 ** 9 + 7)

# much slower solution
'''class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #print(arr)
        total = 0
        modulus = 10 ** 9 + 7
        current = arr[0]
        cachedStart = 0
        cachedEnd = 1
        while cachedEnd < len(arr) and current <= arr[cachedEnd]:
            cachedEnd += 1
        total += cachedEnd * current
        total = total % modulus
        for i in range(1, len(arr)):
            current = arr[i]
            decreased = current < arr[i - 1]
            start = cachedStart if decreased else i
            end = cachedEnd if decreased else i + 1
            while start > 0:
                if current >= arr[start - 1]:
                    break
                start -= 1
            while end < len(arr) and current <= arr[end]:
                end += 1
            #print(f"for {i}: start: {start}, end: {end}, runLeft: {runLeft}, runRight: {runRight}, count: {count}")
            total += (i - start + 1) * (end - i) * current
            if decreased:
                cachedStart = start
                cachedEnd = end
        return total % modulus'''