# Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically 
# next greater permutation of numbers

class Solution:
    def next_perm(self, arr):
        idx = -1
        n = len(arr)
        # finding the first element from right 
        # which is greater than the element on it's left
        for i in range(n - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                idx = i
                break
        
        # if the array is in descending order
        if idx == -1:
            arr.reverse()
        else:
            prev = idx
            
            # finding the element which is just greater than the idx - 1 element
            for i in range(idx + 1, n):
                if arr[i] > arr[idx - 1] and arr[i] <= arr[prev]:
                    prev = i
            # swapping the idx-1 element and the element which is JUST greater than idx-1 element
            arr[idx- 1], arr[prev] = arr[prev], arr[idx - 1]

            # reverse the part from idx to end
            arr[idx:] = reversed(arr[idx:])

            


