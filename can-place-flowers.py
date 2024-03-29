from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            count = 1 if flowerbed[0] == 0 else 0
        else:
            count = 0
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                count += 1
                flowerbed[0] = 1
            i = 1
            while i < len(flowerbed) - 1:
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        count += 1
                        i += 2
                    else:
                        i += 1
                else:
                    i += 2
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                count += 1
        return count >= n