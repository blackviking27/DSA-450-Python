# Dijkstra’s shortest path algorithm

class Graph:
    def __init__(self, v) -> None:
        self.v = v
        self.graph = [[0 for _ in range(v)] for _ in range(v)]
    
    def minDistance(self, dist, sptSet):
        # the minimum distance
        min_dist = float('inf')

        # index of the node with min distnace from the source
        min_index = -1

        for v in  range(self.v):
            if dist[v] < min_dist and v not in sptSet:
                min_dist = dist[v]
                min_index = v
        
        return min_index

    def dijkstraAlgo(self, src):
        # tells us the min distance of each vertex from the source vertex
        dist = [float('inf')]*self.v
        dist[src] = 0

        sptSet = set()

        for _ in  range(self.v):
            # picking the node with the minimum distance from source node
            u = self.minDistance(dist, sptSet)

            # marking the node u as processed
            sptSet.add(u)

            for v in range(self.v):
                if self.graph[u][v] > 0 and v not in sptSet:
                    dist[v] = min(dist[v], dist[u] + self.graph[u][v])
        return dist

 # Driver code

g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ];
dist = g.dijkstraAlgo(0)
for i in range(len(dist)):
    print(f"Vertex {i} is at distnace {dist[i]}")