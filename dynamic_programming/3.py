# Permutation Coefficient
# mathematical formula =>  P(n, k) = P(n-1, k) + k* P(n-1, k-1)  

# getting in O(n) time
def permutationCoefficient(n, k):

    # stores the factorial of numbers from 0 to n
    fact = [0 for i in range(n + 1)]
    fact[0] = 1 # since 0! is 1

    for i in range(1, n+1):
        fact[i] = i * fact[i - 1]
    
    return fact[n] // fact[n - k]

# using the 2d array
def permutation_coefficient_2d(n, k):
    dp = [[0 for i in range(k+ 1)] for j in range(n + 1)]

    for i in range(n+ 1):
        for j in range(min(i,k) + 1):
            if j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = j * dp[i - 1][j -1] + dp[i -1][j]
    return dp[n][k]

print(permutationCoefficient(10, 1))
print(permutation_coefficient_2d(10, 1))