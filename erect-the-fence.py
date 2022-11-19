from typing import List
import math

''' find the convex hull of the set! start at the topmost points, and take the
leftmost of them. then, step repeatedly to the closest next point that lies in
the convex hull (found by comparing dot products). should probably use built
ins or a fast computational library to find magnitudes instead of writing my
own functions
'''
class Solution:
    epsilon = 0.0000001

    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        if len(trees) < 2:
            return trees
        points = [(point[0], point[1]) for point in trees]
        highestY = max([point[1] for point in points])
        # start at the leftmost point at the highest y
        start = min([point for point in points if point[1] == highestY], key=lambda point: point[0])

        convexPoints = set()
        convexPoints.add(start)
        print(start)
        current = self.findClosestConvexPoint(points, start, (start[0] + 1, start[1]))
        previous = start
        while current != start:
            convexPoints.add(current)
            heldCurrent = current
            current = self.findClosestConvexPoint(points, current, previous)
            previous = heldCurrent
        return [[point[0], point[1]] for point in convexPoints]
    
    def findClosestConvexPoint(self, points, parent, parentSibling):
        prevVector = (parent[0] - parentSibling[0], parent[1] - parentSibling[1])
        largestUnitDotFound = -2
        candidates = []
        for point in points:
            if point != parent:
                currentVector = (point[0] - parent[0], point[1] - parent[1])
                dot = prevVector[0] * currentVector[0] + prevVector[1] * currentVector[1]
                unitDot = dot / (self.magnitude(prevVector) * self.magnitude(currentVector))
                if unitDot > largestUnitDotFound + self.epsilon:
                    candidates = [point]
                    largestUnitDotFound = unitDot
                elif abs(unitDot - largestUnitDotFound) < self.epsilon:
                    candidates.append(point)
        return min(candidates, key=lambda point: self.squareMagnitude((point[0] - parent[0], point[1] - parent[1])))

    def squareMagnitude(self, vec):
        return vec[0] * vec[0] + vec[1] * vec[1]

    def magnitude(self, vec):
        return math.sqrt(vec[0] * vec[0] + vec[1] * vec[1])