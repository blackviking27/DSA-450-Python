# 	Detect Negative cycle in a graph
# same as bellman ford

class Solution:
	def bellmanford(self, node):
		self.dist = [float('inf')]*self.n
		self.dist[node] = 0
		
		for i in range(1, self.n):
			for edge in self.edges:
				u, v, w = edge
				if self.dist[u] + w < self.dist[v] and self.dist[u] != float('inf'):
					self.dist[v] = self.dist[u] + w
		
		for edge in self.edges:
			u, v, w = edge
			if self.dist[u] + w < self.dist[v] and self.dist[u] != float('inf') :
				return 1
		return 0

	def isNeagativeCycle(self, n, edges):
		self.n = n
		self.edges  = edges

		self.visited = [False] * self.n
		for i in range(self.n):
			if self.visited[i] == False:
				if self.bellmanford(i):
					return True
				
				for j in range(self.n):
					if self.dist[j] != float('inf'):
						self.visited[i] = True
		return False 