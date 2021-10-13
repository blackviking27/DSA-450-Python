# Minimum Cost of ropes

import heapq as heap


class Solution:
    def minCost(self, arr):
        # convert the array to heap
        heap.heapify(arr)

        cost = 0  # total cost of joining ropes

        while len(arr) > 1:
            a = heap.heappop(arr)
            b = heap.heappop(arr)
            cost += (a + b)
            heap.heappush(arr, a + b)

        return cost
