# Making wired Connections

from collections import defaultdict
class Solution:
    def dfs(self, node):
        self.visited[node] = True
        for i in self.graph[node]:
            if not self.visited[i]:
                self.dfs(i)

    def makeConnected(self, n, connections):
        m = len(connections)
        # if there are n nodes then we require atleast n - 1 edges to make a connected graph
        # thus we are checking if number of connections i.e m is greater than n - 1 or not
        if m < n - 1: return -1

        self.graph = defaultdict(list) # the graph
        
        # mapping the nodes 
        for edge in connections:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])
        
        # to mark a node visited
        self.visited = [False]*n

        cmp = 0 # used for teling the count of components in the graph
        for i in range(n):
            if not self.visited[i]:
                cmp += 1
                # this function wil mark all the node as visited 
                # which are possible to reach from the current ith node
                self.dfs(i)
        return cmp - 1