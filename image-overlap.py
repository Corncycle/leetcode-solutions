from typing import List

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        img1NonzeroCoords = []
        img2NonzeroCoords = []
        for i in range(len(img1)):
            for j in range(len(img2)):
                if img1[i][j] == 1:
                    img1NonzeroCoords.append((i, j))
                if img2[i][j] == 1:
                    img2NonzeroCoords.append((i, j))

        if (img1NonzeroCoords == [] or img2NonzeroCoords == []):
            return 0

        transforms = {}
        for coord1 in img1NonzeroCoords:
            for coord2 in img2NonzeroCoords:
                t = (coord1[0] - coord2[0], coord1[1] - coord2[1])
                if t in transforms:
                    transforms[t] += 1
                else:
                    transforms[t] = 1
        return max(transforms.values())