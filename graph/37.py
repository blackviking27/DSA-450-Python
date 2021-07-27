# Minimum edges to reverse to make path from source to destination

from collections import defaultdict
class Graph:
    def __init__(self, v, e, edges) -> None:
        self.v = v
        self.e = e
        self.edges = edges
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
    
    # function to create reverse edges
    def createReverseEdges(self):
        for u, v in self.edges:
            self.addEdge(u, v, 0) # adding the original edge
            self.addEdge(v, u, 1) # adding the reversed edge
    
    # implementing the dijkstra's algo
    def minDist(self, dist, sptSet):
        min_dist = float('inf')
        min_idx = -1
        for v in range(self.v):
            if dist[v] < min_dist and v not in sptSet:
                min_dist = dist[v]
                min_idx = v
        return min_idx

    def shortestPath(self, src):
        dist = [float('inf')]*self.v
        dist[src] = 0

        sptSet = set()

        for _ in range(self.v):
            u = self.minDist(dist, sptSet)
            sptSet.add(u)

            for v, w in self.graph[u]:
                if v not in sptSet:
                    dist[v] = min(dist[v], dist[u] + w)
        return dist


    # to get minimum reversals
    def minReversalGraph(self, src, dst):
        self.createReverseEdges()
        
        dist = self.shortestPath(src)

        return dist[dst] if dist[dst] != float('inf') else -1

# driver code
V = 7
edges = [[0, 1], [2, 1], [2, 3], [5, 1],[4, 5], [6, 4], [6, 3]]
E = len(edges)
g = Graph(V, E, edges)    
print(g.minReversalGraph(0, 6))
