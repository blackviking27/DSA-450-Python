# Find if there is a path of more than k length from a source

class Solution:
    def __init__(self, v) -> None:
        self.v = v
        self.adj = [[] for _ in range(v)]

    def addEdge(self, u, v, w):
        self.adj[u].append([v, w])
        self.adj[v].append([u, w])

    def pathMoreThanK(self, src, k):
        # to check if a node is already present in the traversal or not
        self.path = [False] * self.v

        # including the src node in the path
        self.path[src] = True

        return self.solve(src, k)

    def solve(self, node, k):
        # we are able to find path more than k length
        if k <= 0:
            return True

        # now going to the adjacent nodes
        for v, w in self.adj[node]:
            # if node 'v' is not visited yet
            if not self.path[v]:

                # marking node 'v' as visited
                self.path[v] = True

                # recursive call
                self.solve(v, k - w)

                # backtracking
                self.path[v] = False
