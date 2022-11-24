from typing import List

class Tree:
    def __init__(self, location, depth):
        self.location = location
        self.depth = depth
        self.children = []
        self.parent = None

    def __str__(self):
        s = str(self.location)
        if self.children:
            s += "\n"
            s += ", ".join([str(child) for child in self.children])
        return s

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for letter in word:
            if not self.letterIsInBoard(board, letter):
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    t = Tree((i, j), 0)
                    depth = self.populateTree(board, word, t)
                    if depth == len(word) - 1:
                        return True
        return False

    def letterIsInBoard(self, board: List[List[str]], letter: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == letter:
                    return True
        return False

    def populateTree(self, board: List[List[str]], word: str, t: Tree):
        frontier = [t]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        maxDepth = 0
        while frontier:
            newFrontier = []
            for node in frontier:
                if node.depth == len(word) - 1:
                    return maxDepth
                for dir in directions:
                    neighborCandidate = (node.location[0] + dir[0], node.location[1] + dir[1])
                    if 0 <= neighborCandidate[0] < len(board) and 0 <= neighborCandidate[1] < len(board[0]):
                        if board[neighborCandidate[0]][neighborCandidate[1]] == word[node.depth + 1]:
                            curr = node
                            while curr and curr.location != neighborCandidate:
                                curr = curr.parent
                            if curr is None:
                                child = Tree((neighborCandidate), node.depth + 1)
                                child.parent = node
                                node.children.append(child)
                                newFrontier.append(child)
                                maxDepth = max(maxDepth, node.depth + 1)
            frontier = newFrontier
        return maxDepth