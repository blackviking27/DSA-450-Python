# Minimum cost to fill given weight in a bag

class Solution:
	def minimumCost(self, cost, N, W):
		val = []
		wt = []
		for i in range(len(cost)):
			if cost[i] != -1:
				val.append(cost[i])
				wt.append(i + 1)
		
		dp = [[0 for i in range(W+1)] for j in range(N+1)]

		# first row price would be infinite
		for i in range(W+1):
			dp[0][i] = float('inf')
		
		# first column would be zero
		for j in range(N+1):
			dp[j][0] = 0
		
		for i in range(1, N+1):
			for j in range(1, W+1):
				if i > j:
					dp[i][j] = dp[i-1][j]
				else:
					dp[i][j] = min(dp[i-1][j], dp[i - 1][j - i] + cost[i-1] if cost[i-1] != -1 else 0)
		return dp[N][W] if dp[N][W] != float('inf') else -1
