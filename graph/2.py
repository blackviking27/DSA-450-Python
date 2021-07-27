# DFS of a graph

class Solution:
    def solve(self, v):
        self.ans.append(v) # append to vertex to the answer
        self.vis[v] = True
        for i in self.adj[v]:
            if not self.vis[i]: # if the vertex is not visited
                self.solve(i)

    def dfsOfGraph(self, V, adj):
        self.ans = []
        # visted array to keep track of visited vertices
        self.vis = [False] * (V)
        self.adj = adj
        self.solve(0)
        return self.ans
