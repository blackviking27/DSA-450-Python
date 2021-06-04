def getNthFromLast(head,n):
    l = 0
    curr = head

    # calculating the length of the linked list
    while curr != None:
        l += 1
        curr = curr.next
    
    # if the target is greater than the total length of the list
    if n > l:
        return -1
    
    # moving till we are at the nth node from end
    temp = head
    for i in range(l-n):
        temp = temp.next
    
    return temp.data

