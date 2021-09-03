# “k” largest element in an array
from queue import PriorityQueue as pq
class Solution:

	def kLargest(self,arr, n, k):
		q = pq()
		for el in arr:
		    q.put(-1 * el)
	    
	    ans = []
	    i = 0
	    while i < k:
	        ans.append(-1 * q.get())
	        i += 1
        return ans