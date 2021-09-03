from queue import PriorityQueue as pq


class Solution:
    def mergeKArrays(self, arr, K):
        ans = []  # to store the sorted list
        q = pq()  # used to create the sorted list

        # storing the first element from every array
        for i in range(K):
            # inserting [val. row, col]
            # row,col will tell us the next element from the current element in
            # the same array
            q.put([arr[i][0], i, 0])

        # now adding all the other values too
        while not q.empty():
            val, row, col = q.get()
            ans.append(val)

            # if it is the last element then we cannot add the next element
            # thus we only go till second last element
            if col < K - 1:
                q.put([arr[row][col + 1], row, col + 1])

        return ans
