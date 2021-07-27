# Prim’s Algorithm

class Graph:
    def __init__(self, v) -> None:
        self.v = v
        self.graph = None
    
    def findMinKey(self):
        min_val = float('inf')
        min_idx = -1
        for i in range(self.V):
            if self.key[i] < min_val and self.mstSet[i] == False:
                min_val = self.key[i]
                min_idx = i
        return min_idx

    def primMST(self, V, adj):
        # adj is adjacency matrix where adj[i][j] is weight of the edge

        self.key = [float('inf')]*V
        self.key[0] = 0
        self.V = V

        # to determine if a node is part of the MST or not
        self.mstSet = [False]*V

        # stores the MST
        parent = [None]*V
        parent[0] = -1

        for _ in range(V):
            # finding the minimum key
            u = self.findMinKey()

            self.mstSet[u] = True

            # key for all the node adjacent to u is updated
            for v in range(self.V):
                if adj[u][v] > 0 and self.mstSet[v] == False:
                    self.key[v] = min(self.key[v], adj[u][v])
                    parent[v] = u
            
        weight_mst = 0
        for i in range(self.V):
            weight_mst += self.key[i]

        return weight_mst