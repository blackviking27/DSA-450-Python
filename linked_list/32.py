# Delete nodes having greater value on right 
# Given a singly linked list, remove all the nodes which have a greater value on its following nodes.

class Solution:
    def reverse(self, head):
        curr = head
        next = None
        prev = None

        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        return prev

    def compute(self, head):
        # reversing the list
        head = self.reverse(head)

        # taking the highes value on right so far
        high = head.data

        prev = head
        curr = head.next

        while curr != None:
            # if the current node data is less than the highest value on right
            # then delete the node
            if curr.data < high:
                curr = curr.next
                prev.next = curr
            else:
                # if the current node is greater or equal to the highest node
                # then update the highest value move both the pointers
                high = curr.data
                prev = curr
                curr = curr.next
        
        head = self.reverse(head)
        return head