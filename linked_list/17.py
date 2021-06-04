# Check if Linked List is Palindrome
# Given a singly linked list of size N of integers. 
# The task is to check if the given linked list is palindrome or not.

class Node:
    def __init__(self, data):
        self.data = data

class Solution:
    def palindrome(self, head):
        # finding the middle element
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        

        # reversing the second part of the linked list
        curr = slow
        prev = None
        next = None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # comparing the 2 halves of the linked list
        fast = head # just assigning the value

        while prev != None:
            if prev.data != fast.data:
                return 0
            fast = fast.next
            prev = prev.next
        
        return 1
