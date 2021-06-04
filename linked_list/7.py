# Move last element to front of a given Linked List

class Solution:
    def move(self, head):
        curr = head
        prev = None

        # Finding the last element in the linked list
        while curr.next != None:
            prev = curr
            curr = curr.next

        # deleting the last element
        prev.next = None
        
        # making the last element as the first element
        curr.next = head
        head = curr

        return head
        
