from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        justTook = set([i for i in range(numCourses)])
        for a, b in prerequisites:
            if a in justTook:
                justTook.remove(a)
        taken = justTook.copy()
        while justTook:
            justTook = set([i for i in range(numCourses)])
            for course in taken:
                if course in justTook:
                    justTook.remove(course)
            for a, b in prerequisites:
                if b not in taken and a in justTook:
                    justTook.remove(a)
            taken = taken.union(justTook)
        return len(taken) == numCourses