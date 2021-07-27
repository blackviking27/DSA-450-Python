# Minimum number of jumps to reach end
class Solution:
	
	# DP approach O(n^2) time
	def minJumps(self, arr, n):
		# stores the min jumps required to reach the ith index
		dp = [float('inf') for i in range(n)]
		dp[0] = 0 # no jumps required to reach the first index

		for i in range(1, n):
			for j in range(i):
				# if we can reach i pos from j pos and if j pos is reachable or not
				if i <= j + arr[j] and dp[j] != float('inf'):
					dp[i] = min(dp[i], dp[j] + 1)
		return dp[n-1]
	
	# Without dynammic programming, O(n) solution
	def minJumps(self, arr, n):
		max_reach = arr[0]
		steps = arr[0]
		jumps = 1
		
		if n == 1: return 0
		if arr[0] == 0: return -1
		
		for i in range(1, n):
			if i == n-1:
				return jumps
			max_reach = max(max_reach, i + arr[i])
			steps -= 1
			if steps == 0:
				jumps += 1
				if i>= max_reach:
					return -1
				steps = max_reach - i
		return -1