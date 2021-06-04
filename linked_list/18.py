# Deletion from a Circular Linked List

class Solution:
    def delete (self, head, key):
        # if the head is empty
        if head is None:
            return

        # if only one node is present
        if head.data == key and head.next == head:
            head = None
        

        curr = head
        prev = None

        # if head needs to be removed
        if head.data == key:
            # finding the last element
            while curr.next != head:
                curr = curr.next
            curr.next = head.next
            head = curr.next
        
        # moving till we find the key
        while curr.next != head and curr.next.data != key:
            curr = curr.next
        
        # removing the target
        if curr.next.data == key:
            curr.next = curr.next.next

        return head

