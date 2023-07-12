from typing import List

# this dfs approach is due to the editorial for the problem
# https://leetcode.com/problems/find-eventual-safe-states/editorial/

class Solution:
    def isUnsafe(self, node, adj, visit, inStack):
        if inStack[node]:
            return True
        if visit[node]:
            return False
        visit[node] = True
        inStack[node] = True
        for neighbor in adj[node]:
            if self.isUnsafe(neighbor, adj, visit, inStack):
                return True
        inStack[node] = False
        return False
    
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = [[] for _ in range(n)]
        
        for i in range(n):
            for node in graph[i]:
                adj[i].append(node)

        visit = [False for _ in range(n)]
        inStack = [False for _ in range(n)]

        for i in range(n):
            self.isUnsafe(i, adj, visit, inStack)

        return [i for i, truth in enumerate(inStack) if not truth]

