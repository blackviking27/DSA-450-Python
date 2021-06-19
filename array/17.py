# Count pairs with given sum 
# Given an array of N integers, and an integer K,
# find the number of pairs of elements in the array whose sum is equal to K.

class Solution:
    def getPairsCount(self, arr, n, k):
        m = {}
        count = 0
        # counting the occurence of each element
        for i in range(n):
            if arr[i] not in m: # if the element occurs for the first time
                m[arr[i]] = 1
            else: # if it is recurring
                m[arr[i]] += 1
        
        # counting pairs
        for i in range(n):
            x = k - arr[i]
            if x in m: # if the element exists in the map
                count += m[x] # since the current element would be paired with every ouccurence of x

                if x == arr[i]: # if x and arr[i] are same then it is the same pair
                    count -= 1

        return count // 2


