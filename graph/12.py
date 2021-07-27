# Topological sort 

from collections import deque
class Solution:
    # BFS approach
    def topoSort(self, V, adj):
        in_degree = [0]*V
        ans = []

        # filling in the in degree value for each node
        for i in range(V):
            # from node i to all the adjacent node contribute 1 in_degree
            for v in  adj[i]:
                in_degree[v] += 1
        
        q = deque()

        # inserting all the vertices which have zero in_degree
        for v in  range(V):
            if in_degree(v) == 0:
                q.append(v)
        
        while q:
            temp = q.popleft()
            ans.append(temp)

            # decreasing the in_degree of adjacent node  by 1 since we have added the current node to ans
            # and that is considered as removing the current node from graph
            for i in adj[temp]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    q.append(i)
        return ans

    # DFS approach
    def dfs(self, node):
        self.visited[node] = True

        # visiting the adjacent nodes of the current node
        for v in self.adj[node]:
            if not self.visited[v]:
                self.dfs(v)

        self.stack.append(node)

    def topologicalSortDFS(self, V, adj):
        self.visited = [False] * V
        self.stack = [] # stores the answer
        self.adj = adj

        for v in range(self.V):
            if not self.visited[v]:
                self.dfs(v)

        return self.stack[::-1]