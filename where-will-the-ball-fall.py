from typing import List

class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        #print(len(grid))
        #print(len(grid[0]))
        '''for row in grid:
            string = ""
            for tile in row:
                string += "\\" if tile == 1 else "/"
            print(string)'''
        balls = [i for i in range(len(grid[0]))]
        for row in grid:
            balls = self.doIteration(balls, row)
        return [self.getIndex(balls, i) for i in range(len(balls))]

    def getIndex(self, balls, i):
        try:
            return balls.index(i)
        except:
            return -1

    def doIteration(self, balls, row):
        prev = row[0]
        for i in range(1, len(row)):
            curr = row[i]
            if prev == 1 and curr == -1:
                balls[i - 1] = -1
                balls[i] = -1
            prev = curr
        balls[0] = -1 if row[0] == -1 else balls[0]
        balls[len(row) - 1] = -1 if row[len(row) - 1] == 1 else balls[len(row) - 1]
        ballsIterated = [-1 for _ in range(len(balls))]
        for i in range(len(balls)):
            if balls[i] > -1:
                ballsIterated[i + row[i]] = balls[i]
        return ballsIterated

s = Solution()
print(s.findBall([[-1,1,-1,-1,-1,-1,-1,-1,1,-1,-1,-1,-1,1,1,-1,-1,-1,1,1,1,-1,-1,1,1,-1,-1,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,-1,-1,-1,1,-1,-1,1,-1,1,-1,-1,1,1,-1,1,-1,-1,-1,-1,1,1,1,1,1,1,-1,1,1,1,-1,1,1,1,-1,-1,-1,1,-1,1,-1,-1,1,1,-1,-1,1,-1,1,-1,1,1,1,-1,-1,-1,-1]]))