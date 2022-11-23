from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(3): # check 3x3 squares
            for j in range(3):
                if not self.checkRegion(board, 3 * j, 3 * i, 3, 3):
                    return False
        for i in range(9): # check rows
            if not self.checkRegion(board, 0, i, 9, 1):
                return False
        for j in range(9): # check columns
            if not self.checkRegion(board, j, 0, 1, 9):
                return False
        return True
    
    def checkRegion(self, board: List[List[str]], startX: int, startY: int, spanX: int, spanY: int) -> bool:
        numbersSeen = 0
        distinctNums = set()
        for i in range(startY, startY + spanY):
            for j in range(startX, startX + spanX):
                if board[i][j] != ".":
                    numbersSeen += 1
                    distinctNums.add(board[i][j])
        return numbersSeen == len(distinctNums)