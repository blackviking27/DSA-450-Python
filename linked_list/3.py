# Remove loop in Linked List

class Solution:
    def delete_loop(self, head):

        # trying to detect if loop is present or not
        low = head
        high = head

        while high != None and high.next != None:
            low = low.next
            high = high.next.next

            if low == high:
                break
        
        # if both low and high reach the head pointer, then we just need to move the high pointer
        if low == head:
            while high.next != low:
                high = high.next
            high.next = None
        
        elif low == high: # checking of loop is present or not
            low = head
            # finding the starting point of the loop
            while low.next != high.next:
                low = low.next
                high = high.next
            
            high.next = None