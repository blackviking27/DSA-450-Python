# Intersection of two sorted Linked lists
# Given two lists sorted in increasing order, create a new list representing the intersection of the two lists. 
# The new list should be made with its own memory — the original lists should not be changed

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def intersection(self, first, second):
        i = first
        j = second

        res = None
        curr = None
        while i != None and j != None:
            if i.data == j.data:
                temp = Node(i.data)
                if res == None:
                    res = temp
                else:
                    curr.next = temp
                curr = temp
                i = i.next
                j = j.next
            elif i.data < j.data:
                i = i.next
            else:
                j = j.next
        return res

