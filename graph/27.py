# Check whether a graph is Bipartite or Not

from collections import deque
class Solution:
    # taking adjacency list
    def solve(self, node):
        self.q.append(node)
        self.color[node] = 0

        while self.q:
            u = self.q.popleft()
            # changing the color of the neighbor nodes to opposite color
            for v in self.adj[node]:
                if self.color[v] == self.color[u]:
                    return False

                if self.color == -1:
                    self.color[v] = 0 if self.color[u] else 1
                    self.q.append(v)
        return True

    def isBipartite(self, V, adj):
        # stores the color for each node
        self.color = [-1]*V
        self.adj = adj
        self.q = deque()

        for i in range(V):
            if self.color[i] == -1:
                if not self.solve(i):
                    return False
        return True