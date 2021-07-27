# Graph Coloring

from collections import defaultdict
class Graph:
    def __init__(self, v) -> None:
        self.v = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def minColor(self):
        
        # chromatic number
        cn = 0

        # stores the color of each node
        # the first node has color 0 
        res = [-1]*self.v
        res[0] = 0
        
        # tells us if a color is available or not
        available = [False]*self.v

        for u in range(1, self.v):
            # checking if the adjacent nodes are colored or not
            for v in self.graph[u]:
                # if node is colored then make that color as 
                # unavailable for node u
                if res[v] != -1: 
                    available[res[v]] = True
            
            # now finding the available color for node u
            cr = 0
            for i in range(self.v):
                if available[i] == False:
                    cr = i
                    break
            
            # updating the answer
            res[u] = cr

            # updating the chromatic number
            cn = max(cn, cr + 1)

            # making the unavailable colors available again
            for v in self.graph[u]:
               if res[v] != -1:
                available[res[v]] = False

        print(f"Chromatic Number is {cn}")
        print("Colors assigned is ", res)

g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(0, 2)
g.addEdge(2, 4)
g.addEdge(1, 4)
# g.addEdge(0, 4)

g.minColor()