# Strongly Connected Components (Kosaraju's Algo) 

class Solution:
    def fill_order(self, node):
            self.visited[node] = True
            for i in self.adj[node]:
                if self.visited[i] == False:
                    self.fill_order(i)

            self.stack.append(node)
    
    # DFS function to traverse the reverse graph
    def dfs(self, node):
        self.visited[node] = True
        for i in self.reverse_graph[node]:
            if self.visited[i] == False:
                self.dfs(i)

    def kosaraju(self, V, adj):
        # creating the vertex order
        self.adj = adj
        self.stack = []
        self.visited = [False]*V

        for i in range(V):
            if self.visited[i] == False:
                self.fill_order(i)

        # creating a reverse graph
        self.reverse_graph = [[] for _ in range(V)]
        for i in range(V):
            for v in adj[i]:
                self.reverse_graph[v].append(i)
        
        # counting strongly connected graph
        self.visited = [False]*V

        count = 0
        while self.stack:
            v = self.stack.pop()
            if self.visited[v] == False:
                count += 1
                self.dfs(v)
        return count
