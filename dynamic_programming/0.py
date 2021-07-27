# Coin Change 

class Solution:
    # iterative approach
    def count_itr(self, arr, m, n): 
        # table[i] stores the number of solutions for value i
        table = [0 for i in range(n + 1)]
        table[0] = 1 # initial case, number of ways to get sum 0 is 1
        for i in range(m):
            for j in range(arr[i], n + 1):
                table[j] += table[j - arr[i]]
        return table[n]

    # recursive approach
    def solve(self, arr, m, n):
        if m == -1 and n > 0:# if m is over and sum is still not reachable
            return 0
        if n==0:# if we are able to satisfy the sum
            return 1
        if n < 0: # if sum is negative
            return 0
        
        if self.dp[m][n] != -1: return self.dp[m][n] # if alreadt calculated

        # if not then calculate for when coin is included and coin is excluded and add the sum
        self.dp[m][n] = self.solve(arr, m, n - arr[m]) + self.solve(arr, m -1, n)
        return self.dp[m][n]
    
    def count(self, arr, m, n): 
        # create a dp which stores the sum for each coin
        #  ex: if n = 4 and m = 3, {1,2,3}
        # then initial dp would look like
        #    0  1  2  3  4
        #  0 -1 -1 -1 -1 -1 
        #  1 -1 -1 -1 -1 -1
        #  2 -1 -1 -1 -1 -1
        #  3 -1 -1 -1 -1 -1
        # it shows that for ith coin and jth sum n number of ways are possible
        self.dp = [[-1 for i in range(n + 1)] for i in range(m)] 
        return self.solve(arr, m - 1, n)