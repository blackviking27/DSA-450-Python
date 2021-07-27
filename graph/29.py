# Longest path in a Directed Acyclic Graph

from collections import defaultdict, deque
class Graph:
    def __init__(self, v) -> None:
        self.v = v 
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # topological sort
    def topologicalSort(self, node):
        self.visited[node] = True
        for v in self.graph[node]:
            if self.visited[v[0]] == False:
                self.topologicalSort(v[0])
        
        self.stack.append(node)

    # longest path function
    def longestPath(self, src):
        self.visited = [False]*self.v
        dist = [float('-inf')]*self.v
        self.stack = []

        for i in range(self.v):
            if self.visited[i] == False:
                self.topologicalSort(i)
        
        # distance of source node is zero
        dist[src] = 0

        while len(self.stack) > 0:
            # taking the top element
            top = self.stack.pop()

            if dist[top] != float('-inf'):
                # updating distance for all the adjacent nodes
                for v in self.graph[top]:
                    if dist[v[0]] < dist[top] + v[1]:
                        dist[v[0]] = dist[top] + v[1]
        
        print(dist)

g = Graph(7)

g.addEdge(0, [1, 5])
g.addEdge(0,[2, 3])
g.addEdge(1,[3, 6])
g.addEdge(1,[2, 2])
g.addEdge(2,[4, 4])
g.addEdge(2,[5, 2])
g.addEdge(2,[3, 7])
g.addEdge(3,[5, 1])
g.addEdge(3,[4, -1])
g.addEdge(4,[5, -2])

src = 1
g.longestPath(src)



