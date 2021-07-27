# Detect Cycle in Directed Graph using BFS/DFS Algo

class Solution:
    # using the DFS appraoch
    def findCycle(self, v):
        self.vis[v] = True
        self.order[v] = True

        # traversing the child nodes of the current node
        for i in self.adj[v]:
            if not self.vis[i]:
                conf = self.findCycle(i)
                if conf == True:
                    return True
            elif self.order[i]: # if the node is already visited and is present in the current order
                return True
        
        self.order[v] = False
        return False

    def isCyclicDFS(self, V, adj):
        self.vis = [False] * (V + 1)
        self.order = [False] * (V + 1)
        self.adj = adj

        # checking the cycle for each node
        for i in range(V):
            if self.vis[i] == False:
                if self.findCycle(i) == True:
                    return True
        return False
