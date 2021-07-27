# Check if a given graph is tree or not


from collections import defaultdict
class Graph:
    def __init__(self, V) -> None:
        self.V = V
        self.graph = defaultdict(list)
    
    def addEdge(self, v, w):
        # graph is a dict object which stores all the nodes mapped to the current node
        # v, w are the index value 
        self.graph[v].append(w)
        self.graph[w].append(v)
    
    def isCyclic(self, v, visited, parent):
        visited[v] = True # v is the index  of the node

        # for all the nodes that are connected to the current node
        for i in self.graph[v]:
            # if it is not visited
            if visited[i] == False:
                if self.isCyclic(i, visited, v) == True:
                    return True
            elif i != parent:
                return True
        return False

    def isTree(self):
        visited = [False] * self.V # since each node is not visited initially

        if self.isCyclic(0, visited, -1):
            return False
        
        # if any of the node is not visited then it is not a tree
        for i in range(self.V):
            if visited[i] == False:
                return False
        return True

# Driver Program
g1 = Graph(5)
g1.addEdge(1, 0)
g1.addEdge(0, 2)
g1.addEdge(0, 3)
g1.addEdge(3, 4)

if g1.isTree():
    print("It is a tree")
else:
    print("It is not a tree")

g2 = Graph(5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)

if g2.isTree():
    print("It is a tree")
else:
    print("It is not a tree")