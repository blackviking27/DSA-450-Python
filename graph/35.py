# Find if there is a path of more than k length from a source

from collections import defaultdict
class Graph:
    def __init__(self, v):
        self.v = v
        self.adj = defaultdict(list)
    
    def addEdge(self, u, v, w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])
    
    def findPath(self, node, k):
        self.visited[node] = True
        if k <= 0: return True

        for v, w in self.adj[node]:
            if self.visited[v] == True:
                continue
                
            if w >= k:
                return True
            
            if self.findPath(v, k - w):
                return True
        
        self.visited[node] = False
        return False

    def pathMoreThanK(self, src, k):
        
        # to check if a node is visited or not
        self.visited = [False]*self.v
        return self.findPath(src, k)

# driver code
g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 2, 8)
g.addEdge(1, 7, 11)
g.addEdge(2, 3, 7)
g.addEdge(2, 8, 2)
g.addEdge(2, 5, 4)
g.addEdge(3, 4, 9)
g.addEdge(3, 5, 14)
g.addEdge(4, 5, 10)
g.addEdge(5, 6, 2)
g.addEdge(6, 7, 1)
g.addEdge(6, 8, 6)
g.addEdge(7, 8, 7)

src = 0
k = 62

if g.pathMoreThanK(src, k):
    print("Yes")
else:
    print("No")

k = 60
if g.pathMoreThanK(src, k):
    print("Yes")
else:
    print("No")