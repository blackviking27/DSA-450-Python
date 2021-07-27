# Minimize the Heights II 
# Given an array arr[] denoting heights of N towers and a positive integer K, 
# you have to modify the height of each tower either by increasing or decreasing them by K only once. 
# After modifying, height should be a non-negative integer. 
# Find out what could be the possible minimum difference of the height of shortest 
# and longest towers after you have modified each tower.

class Solution:
    def get_min_diff(self, arr, n, k):
        # n is the length of array
        # k is the size by which we cab cut down the tree
        v = []
        vis = [0]*n

        # inserting each element's variation along with index
        for i in range(n):
            if arr[i] - k >= 0:
                v.append([arr[i] - k, i]) # naegative variation
            v.append([arr[i] + k, i]) # positive variation
        
        v.sort() # sorting the array according to the heights

        ele = 0
        left = 0
        right = 0

        # finding the sub array in v, which contains all the n heights
        # If both negative and psotive variant is present then they will be counted as one
        while ele < n and right < len(v):
            if vis[v[right][1]] == 0: # the element is appearing for the first time
                ele += 1
            vis[v[right][1]] += 1 # incrementing the number of times the nth tree is visited
            right += 1 # moving to the next tree
        
        # when we get first n tree together we calculate the diff
        ans = v[right - 1][0] - v[left][0] # taking right - 1 since we inremented by 1 before breaking the loop

        # now trying to find the next min diff
        while right < len(v):
            if vis[v[left][1]] == 1: # if the left element has occured only once in the sub array
                ele -= 1
            vis[v[left][1]] -= 1
            left += 1

            # again find the n trees together
            while ele < n and right < len(v):
                if vis[v[right][1]] == 0:
                    ele += 1
                vis[v[right][1]] += 1
                right += 1
            
            if ele == n: # if we find n trees together in the sub array
                ans =  min(ans, v[right - 1][0] - v[left][0])
            else: # if we did not find the n trees together again
                break
        return ans

        


