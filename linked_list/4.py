# Find first node of loop in a linked list
# Write a function findFirstLoopNode() that checks whether a given Linked List contains a loop. 
# If the loop is present then it returns point to the first node of the loop. Else it returns NULL.

# The solution is same as the delete the loop question, but in this we need to return the point
class Solution:
    def first_node(self, head):
        low = head
        high = head

        while high.next != None and high != None:
            low = low.next
            high = high.next.next

            if low == high:
                break
        # if first node of the loop is head pointer itself
        if low == head:
            return head
        
        elif low == high:
            low = head
            while low.next != high.next:
                low = low.next
                high = high.next

            # when both low and high point at the same node, then that node is the first node
            # of the loop
            return high.next
        
        # if we don't find any loop
        return None 