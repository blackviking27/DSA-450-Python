# Middle of the Linked List
# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

class Solution:
    def middle(self, head):
        slow = head
        fast = head.next

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow