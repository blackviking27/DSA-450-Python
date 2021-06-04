# Add two numbers represented by linked lists
# Given two numbers represented by two linked lists of size N and M. The task is to return a sum list. 
# The sum list is a linked list representation of the addition of two input numbers from the last.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:

    # reversing a given linked list
    def reverse(self, head):
        curr = head
        prev = None
        next = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
    def add_two_ll(self, first, second):
        first = self.reverse(first)
        second = self.reverse(second)

        c = 0 # carry
        s = 0 # sum

        res = None
        curr = None

        while first != None or second != None:
            s = c + ( first.data if first else 0 ) + (second.data if second else 0) # checking if the node exist, if it does not then we take 0 as its value 
            c = ( 1 if s >= 10 else 0 ) # if sum is greater than 10 then carry is 1 else it is zero

            s = s % 10

            # creating the new linked list
            temp = Node(s)

            # declaring the head of the new linked list
            if res == None:
                res = temp
            else: 
                curr.next = temp # adding the new node, temp.
            curr = temp

            # moving the nodes
            if first: first = first.next
            if second: second = second.next

        # if carry is left
        if c > 0:
            temp = Node(c)
            curr.next = temp
            curr = temp
        
        # reversing the list to get the correct order
        res = self.reverse(res)
        return res







