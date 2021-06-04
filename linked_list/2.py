# Detect Loop in linked list 

# according to the GFG problem
class Solution:
    # Function to check if the linked list has a loop.
    def detectLoop(self, head):
        curr = head
        while curr is not None:
        # Each element data is made negative for each visit,
        # if a negative value is encountered then the node was already visited
            if curr.data > 0:
                curr.data *= -1
            else:
                return True
            curr = curr.next
        return False

    # Floyd’s Cycle-Finding Algorithm:  
    def floyd_cycle(self, head):
        if head is None:
            return False
        
        low = head # this will increment by 1
        high = head # this will increment by 2

        while high != None and high.next != None:
            low = low.next
            high = high.next.next
            if low == high:
                return True
        
        return False