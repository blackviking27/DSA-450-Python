# Maximum sum rectangle in a 2D matrix

class Solution:
    def kadene(self, arr, n):
        max_sum = float('-inf')
        max_till_here = 0
        for i in range(n):
            max_till_here += arr[i]
            max_sum = max(max_sum, max_till_here)
            
            if max_till_here < 0:
                max_till_here = 0
        return max_sum
    
    def maximumSumRectangle(self,R,C,M):
        max_sum = float('-inf')
        for i in range(R):
            ans = [0] * C
            for j in range(i, R):
                for col in range(C):
                    ans[col] += M[j][col]
                max_sum = max(max_sum, self.kadene(ans, C))
        return max_sum