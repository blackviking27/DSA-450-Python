# Detect cycle in an undirected graph 

class Solution:
	def isCyclePresent(self, v, parent):
		self.vis[v] = True

		for i in self.adj[v]:
			if not self.vis[i]:
				if self.isCyclePresent(i, v) == True:
					return True
			elif parent != i: return True
		return False

	def isCycle(self, V, adj):
		self.vis = [False] * V
		self.adj = adj
		for i in range(V):
			if not self.vis[i]:
				if self.isCyclePresent(i, -1) == True:
					return True
		return False
		