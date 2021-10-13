# Median in a stream of Integers

from queue import PriorityQueue as pq


class Solution:
    def __init__(self) -> None:
        self.max_heap = pq()  # stores the left half of soreted array
        self.min_heap = pq()  # stroes the right half of sorted array

    def getMedian(self):
        l = len(self.max_heap.queue)
        r = len(self.min_heap.queue)

        if l > r:
            return -1 * self.max_heap.queue[0]
        else:
            return (self.min_heap.queue[0] + (-1 * self.min_heap.queue[0])) / 2

    def insertHeap(self, x):
        # getting length of max_heap and min_heap
        l = len(self.max_heap.queue)
        r = len(self.min_heap.queue)

        # if both are empty
        # since we are assuming that max_heap will have a size atmost 1 greater than min_heap
        # thus if max_heap is zero then min_heap is also zero
        if l == 0:
            # multiply by 1 to make it a max heap
            self.max_heap.put(-1 * x)
        # if both min_heap and max_heap have same size
        elif l == r:
            # if the element lies in the max_heap then just push it
            if x <= -1 * self.max_heap.queue[0]:
                self.max_heap.put(-1 * x)
            # if the element lies in the right half then push the top of min_heap
            # into the max heap and then push the current element to min_heap
            else:
                temp = self.min_heap.get()
                self.max_heap.put(-1 * temp)
                self.min_heap.put(x)
        # if length of max_heap is greater than min_heap
        else:
            # if second element is being inserted
            if r == 0:
                if x > -1 * self.max_heap.queue[0]:
                    self.min_heap.put(x)
                else:
                    temp = -1 * self.max_heap.get()
                    self.max_heap.put(-1 * x)
                    self.min_heap.put(temp)
            # if the element can be inserted in min_heap the we just insert the element
            # into the heap sinc now the size of both heaps would be equal
            elif x >= self.min_heap.queue[0]:
                self.min_heap.put(x)
            # if want to insert into max_heap then we move the top element of max_heap
            # into the min heap and insert the current element into max_heap
            else:
                if x < -1 * self.max_heap.queue[0]:
                    temp = -1 * self.max_heap.get()
                    self.min_heap.put(temp)
                    self.max_heap.put(-1 * x)
                else:
                    self.min_heap.put(x)
