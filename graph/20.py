# Implement Bellman Ford Algorithm
# bellman ford algo can be used to detect negative cycle

class Solution:
	def isNegativeWeightCycle(self, n, edges): 
		dist = [float('inf')]*n
		dist[0] = 0

		# run the loop n - 1 times
		# to find the shortest path to a node from node 0 i.e source node
		for _ in range(n - 1):
			for edge in edges:
				u, v, w = edge
				if dist[u] != float('inf') and dist[v] > dist[u] + w:
					dist[v] = dist[u] + w
		
		# to find the negative cycle
		for edge in edges:
			u, v, w = edge

			# if there is a negative cycle
			if dist[u] != float('inf') and dist[v] > dist[u] + w:
				return 1
		return 0