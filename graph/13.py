# Minimum time taken by each job to be completed given by a Directed Acyclic Graph

from collections import defaultdict, deque
class Graph:
    def __init__(self, vertices, edges) -> None:
        self.n = vertices
        self.m = edges
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def minTime(self, n , m):
        
        in_degree = [0]*(n + 1) # since they have 1-based indexing
        for i in range(n):
            for v in self.graph[i]:
                in_degree[v] += 1
        
        q = deque()
        # stores the time at which the job is completed
        jobs = [0]*(n + 1) 

        for v in range(1, n + 1):
            if in_degree[v] == 0:
                q.append(v)
                jobs[v] = 1
        
        while q:
            temp = q.popleft()
            for v in self.graph[temp]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    jobs[v] = jobs[temp] + 1
                    q.append(v)

        print(*jobs)
        
# Driver Code

n = 10
m = 13

g = Graph(n, m)

# adding edges
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(2, 3)
g.addEdge(2, 8)
g.addEdge(2, 9)
g.addEdge(3, 6)
g.addEdge(4, 6)
g.addEdge(4, 8)
g.addEdge(5, 8)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 10)

g.minTime(n, m)
