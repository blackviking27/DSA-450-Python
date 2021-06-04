# Check If Circular Linked List

def isCircular(head):
    # since an empty linked list is a circular linked list
    if head == None:
        return 1

    temp = head
    # moving till we find the head again
    while temp.next != head:
        temp = temp.next
        if temp == None:
            return 0
    # if we reach the head
    return 1