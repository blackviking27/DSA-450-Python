# Triplet Sum in Array
# Given an array arr of size n and an integer X. 
# Find if there's a triplet in the array which sums up to the given integer X.

class Solution:
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to X.
    def find3Numbers(self, arr, n, X):
        arr.sort() # sorting the array
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                if arr[i] + arr[j] + arr[k] == X:
                    return True
                elif arr[i] + arr[j] + arr[k] < X:
                    j += 1
                else:
                    k -= 1
        return False