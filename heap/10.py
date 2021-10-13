# Smallest range in “K” Lists

from queue import PriorityQueue as pq


class Solution:
    def smallestRange(self, arr, n, k):
        q = pq()  # stores the values from the range

        high = float('-inf')  # to know the max in range

        # inserting the first element from each array
        for i in range(k):
            # insert val, row, col
            # row -> array number, col -> position in array
            # we can also add a fourth value 'length' which would tell the length of the array
            # that the element belongs to, incase we have arrays of different size
            q.put([arr[i][0], i, 0])
            high = max(high, arr[i][0])

        min_low = 0  # min low in answer range
        max_low = 0  # max high in answer range

        min_range = float('inf')  # the answer range length

        while not q.empty():
            val, row, col = q.get()

            # the current popped value can be the new min since the min value is popped from the min heap
            if min_range > high - val:
                min_range = high - val

                min_low = val
                min_high = high

            # if the current element is the last element in its array then break
            if col == n - 1:
                break

            # inserting the next element
            q.put([arr[row][col + 1], row, col + 1])
            # if the new inserted value is greater than the current max in heap
            high = max(high, arr[row][col + 1])

        return [min_low, min_high]
