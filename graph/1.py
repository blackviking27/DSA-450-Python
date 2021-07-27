# BFS of a graph

from collections import deque
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        ans = []
        vertices = deque([0]) # taking the first element
        visited = [False]*(V + 1)
        visited[0] = True
        while len(vertices) != 0:
            temp = vertices.popleft() # removing the element at top
            ans.append(temp)
            for i in adj[temp]:
                if visited[i] == False:
                    vertices.append(i)
                    visited[i] = True
        return ans


