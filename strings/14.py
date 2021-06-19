# Next Permutation

class Solution:
    def nextPermutation(self, n, arr):
        # code here
        idx = -1 # index of element which is greater than it's left element

        # finding idx value
        for i in range(n - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                idx = i
                break
        # if we don't find the idx i.e arr is in descending order
        # then reverse the array
        if idx == -1:
            arr.reverse()
        else:
            prev = idx
            # finding the correct position of idx -1 element
            for i in range(idx + 1, n):
                if arr[i] > arr[idx - 1] and arr[i] <= arr[prev]:
                    prev = i
            
            # swap the elements
            arr[idx - 1], arr[prev] = arr[prev], arr[idx - 1]

            # reverse the arr from idx to end
            arr[idx:] = reversed(arr[idx:])
        return arr