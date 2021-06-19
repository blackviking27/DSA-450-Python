# Three way partitioning

class Solution:
	def threeWayPartition(self, arr, a, b):
	    n = len(arr)
	    start = 0 # tracks value less than low value of range
	    end = n - 1 # tracks value greater than high value of range
	    i = 0 # for traversing the array
	    while i <= end:
            # if the current element is less than lower of range
	        if arr[i] < a:
	            arr[i], arr[start] = arr[start], arr[i]
	            i += 1
	            start += 1
            # if the current element is greater than higher of range
	        elif arr[i] > b:
	            arr[i], arr[end] = arr[end], arr[i]
	            end -= 1
	        else:
	             i += 1