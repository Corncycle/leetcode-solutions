from typing import List
from collections import deque
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tupTasks = deque(sorted([tuple(task) + (i,) for i, task in enumerate(tasks)]))
        availTasks, order = [], []
        currTime = 0
        while True:
            if availTasks:
                duration, index = heapq.heappop(availTasks)
                currTime += duration
                order.append(index)
            while tupTasks and tupTasks[0][0] <= currTime:
                avail = tupTasks.popleft()
                heapq.heappush(availTasks, (avail[1], avail[2]))
            if not availTasks:
                if not tupTasks:
                    return order
                currTime = tupTasks[0][0]