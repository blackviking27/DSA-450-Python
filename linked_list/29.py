# Clone a linked list with next and random pointer

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None
        self.arb = None

class Solution:
    def copyList(seld, head):
        
        # adding a copy of each after the node in the original linked list
        curr = head
        temp = None
        while curr != None:
            temp = curr.next
            curr.next = Node(curr.data)
            curr.next.next = temp
            curr = temp
        
        # fixing the arbitary pointers of the copied node
        curr = head
        while curr != None:
            curr.next.arb = curr.arb.next if curr.arb else curr.arb
            curr = curr.next.next

        # Removing the link between the original and copied linked list
        original = head
        copy = head.next
        temp = head.next # head of the copied linked list
        while original != None and copy != None:
            original.next = original.next.next # the original node's next is now pointing to the next node in original list
            copy.next = copy.next.next if copy.next else copy.next # copied node's next 
            original = original.next
            copy = copy.next
        
        return temp
