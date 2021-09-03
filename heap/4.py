import heapq


class Solution:
    # using the heap method
    def kthSmallest(self, arr, l, r, k):
        heapq.heapify(arr)

        # add to the min heap and pop k times
        for el in arr:
            heapq.heappush(arr, el)

        for i in range(k - 1):
            heapq.heappop(arr)

        return arr[0]
