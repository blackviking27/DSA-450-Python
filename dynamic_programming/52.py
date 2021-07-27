# Mobile Numeric Keypad Problem [ IMP ]

class Solution:
	def solve(self, i, j, n):
		if n == 1: return 1
		if self.dp[self.keypad[i][j]][n] != -1: return self.dp[self.keypad[i][j]][n]

		# when we press the same key
		a = self.solve(i, j, n - 1)
		b = c = d = e = 0
		if j - 1 >= 0 and self.keypad[i][j -1] != -1:
			b = self.solve(i, j - 1, n - 1)
		
		if j + 1 < 3 and self.keypad[i][j + 1] != -1:
			c = self.solve(i, j + 1, n - 1)
		
		if i - 1 >= 0 :
			d = self.solve(i - 1, j, n - 1)
		
		if i + 1 < 4 and self.keypad[i+1][j] != -1:
			e = self.solve(i + 1, j, n - 1)
		
		self.dp[self.keypad[i][j]][n] = a + b + c + d + e
		return self.dp[self.keypad[i][j]][n]

	def getCoun(self, n):
		
		self.keypad = [[1,2,3]
						[4,5,6]
						[7,8,9]
						[-1,0,-1]]

		self.dp = [[-1 for _ in range(n + 1)] for _ in range(10)]
		ans = 0
		for i in range(4):
			for j in range(3):
				if self.keypad[i][j] != -1:
					ans += self.solve(i, j, n)
		return ans