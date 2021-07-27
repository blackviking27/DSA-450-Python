# Kruksal’sAlgorithm

class Graph:
    def __init__(self, vertices) -> None:
        self.v = vertices
        self.graph = []

    # append edges
    def addEdge(self, u, v, w):
        self.graph.append([u,v,w])

    # function to find the parent of a node in disjoint set
    def find(self, node):
        if self.parent[node] == node:
            return node
        return self.find(self.parent[node])
    
    # create the union of the set
    def union(self, x, y):
        # find the absolute  parent node of x, y
        xroot = self.find(x)
        yroot = self.find(y)

        # Attach the smaller rank tree under the higher rank tree
        if self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        elif self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:# if the both the node have same rank
            self.parent[yroot] = xroot
            self.rank[xroot] += 1


    # MST function
    def kruskalMST(self):
        # sorting the edges
        self.graph.sort(key = lambda x: x[2])

        # storing the answer
        ans = []

        # keeps track of the sets
        self.parent = []

        # keeps track of sets which are suppose to have more priority than other
        self.rank = []

        # each  node is parent of itself
        for node in range(self.v):
            self.parent.append(node)
            self.rank.append(0)

        i = 0 # points to the edge in the sorted edges
        e = 0 # keeps the count of edges that are included in the MST

        while e < self.v - 1:
            u, v, w = self.graph[i]
            i += 1
            # find the parent node of u and v
            x = self.find(u)
            y = self.find(v)

            # if both node belong to different set
            if x != y:
                ans.append([u,v,w])
                e += 1
                # join the two sets i.e create a union of the two sets
                self.union(x, y)
        
        total_weight = 0
        for i in ans:
            total_weight += i[2]
            print(f"Weight of Edge {i[0]} ==> {i[1]} : {i[2]} ")
        print(f"Total weight of MST : {total_weight}")

# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

g.kruskalMST()