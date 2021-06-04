# Reverse a Doubly Linked List

def reverse(head):
    curr = head
    
    # checking if the list is empty or does it only contain a single element
    if curr == None or curr.next == None:
        return head
    
    while curr.next != None:
        curr = curr.next

    # last eleement is the head now
    head = curr

    # swapping the next and prev of the elements
    while curr != None:
        curr.next, curr.prev = curr.prev, curr.next
        curr = curr.next
    
    return head