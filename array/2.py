# Kth smallest element

from queue import PriorityQueue

class Solution:
    def kth(self, arr, target):
        n = len(arr)
        pq = PriorityQueue()
        for i in range(n):
            pq.put(arr[i])
        # finding the kth smallest element
        k = 0
        ans = 0
        while not pq.empty():
            ans = pq.get()
            k += 1
            if k == target:
                return ans
        return -1