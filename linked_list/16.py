# Split a Circular Linked List into two halves
# Given a Cirular Linked List of size N, split it into two halves circular lists. 
# If there are odd number of nodes in the given circular linked list then out of the 
# resulting two halved lists, first list should have one node more than the second list. 
# The resultant lists should also be circular lists and not linear lists.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        ptr = Node(data)
        temp = self.head

        ptr.next = self.head # pointing to the head

        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr
        else:
            ptr.next = ptr
        self.head = ptr

    def split(self, head1, head2):
        slow = self.head
        fast = self.head

        # if head is None
        if self.head is None:
            return
        
        # finding the middle node
        # if odd no of nodes then fast.next will be head
        # if even no of nodes then fast.next.next will be head
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next
        
        # moving the fast pointer to the last element
        if fast.next.next == self.head:
            fast = fast.next

        # initialising head1
        head1 = self.head

        # initialising head2
        if self.head.next != self.head:
            head2 = slow.next
        
        fast.next = slow.next
        slow.next = self.head
        



