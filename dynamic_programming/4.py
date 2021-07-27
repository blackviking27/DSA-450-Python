# Program for nth Catalan Number

class Solution:
    # O(n^2) solution
    def n_catalan(self, n):
        if n == 0 or n == 1:
            return 1
        
        # stores the catalan value
        # at index 0 catalan(0) value would be stored
        catalan = [0]*(n+1)

        catalan[0] = 1
        catalan[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                catalan[i] += catalan[j]*catalan[i-j + 1]

        return catalan[n] 

    # catalan number using the binomial coefficient
    def n_catalan_binomial(self, n):
        # we can calculate the catalan number with binomial coefficient too
        # catalan = C(2n, n ) / (n + 1)
        if n == 0 or n == 1:
            return 1

        # calculating the binomial coefficient for 2*n, n
        res = 1

        for i in range(n):
            res = res * (2*n - i)
            res = res / (i + 1)

        return res / (n + 1)