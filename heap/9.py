# Merge K sorted linked lists


import sys
from queue import PriorityQueue as pq


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


# for min heap approach

# for gfg platform
sys.setrecursionlimit(10**8)


# without min heap approach
class Solution1:

    def merge(self, left, right):
        if left is None:
            return right
        if right is None:
            return left

        res = None
        if left.data <= right.data:
            res = left
            res.next = self.merge(left.next, right)
        else:
            res = right
            res.next = self.merge(left, right.next)
        return res

    def mergeKLists(self, arr, K):
        last = K - 1  # taking the last element
        while last != 0:
            i = 0
            j = last
            while i < j:
                arr[i] = self.merge(arr[i], arr[j])

                i += 1
                j -= 1
                if i >= j:
                    last = j

        return arr[0]


class Solution:
    def mergeKLists(self, arr, k):
        q = pq()

        # inserting the first node of every linked list to min heap
        for i in range(k):
            if arr[i] != None:
                q.put([arr[i].data, arr[i]])

        res = Node(-1)  # to store the sorted linked list
        curr = res  # to point to the end
        # print(q.queue)
        while not q.empty():

            val, node = q.get()
            curr.next = node
            curr = curr.next

            # print(q.queue)
            if node.next != None:
                q.put([node.next.data, node.next])

        return res.next
