# Find whether it is possible to finish all tasks or not from given dependencies

from collections import defaultdict

class Solution:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
    
    def connect(self, pair):
        # connecting the graph
        self.graph[pair[1]].append(pair[0])

    def visit(self, node):
        self.visited[node] = True
        self.order[node] = True

        for v in self.graph[node]:
            if not self.visited[v]:
                if self.visit(v):
                    return True
            elif self.order[v]: return True
        
        self.order[node] = False
        return False

    def isCyclic(self):
        # we can complete all the tasks if we dont find a cycle in the graph

        self.visited = [False]*(self.v + 1)
        self.order = [False]*(self.v + 1)

        for v in range(self.v):
            if not self.visited[v]:
                if self.visit(v):# if cycle is present
                    return True
        return False

# driver code

g = Solution(3)
g.connect([1, 0])
g.connect([2, 1])
g.connect([3, 2])

if not g.isCyclic():
    print("All tasks completed")
else:
    print("Cannot complete all tasks")