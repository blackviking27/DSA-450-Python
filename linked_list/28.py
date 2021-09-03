# Given a linked list of 0s, 1s and 2s, sort it. 
# Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. 
# The task is to segregate 0s, 1s, and 2s linked list such that all zeros 
# segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Solution:

    # Without chaning links
    def segregate(self, head):
        curr = head
        count = {0: 0, 1: 0, 2: 0}

        while curr != None:
            count[curr.data] += 1
            curr = curr.next
        
        i = 0
        curr = head
        while curr != None:
            if count[i] == 0:
                i += 1
            else:
                curr.data = i
                curr = curr.next
                count[i] -= 1
        return head

    # with changing the links
    def segregate_links(self, head):
        # creating head for each value
        zero_head = Node(-1)
        one_head = Node(-1)
        two_head = Node(-1)

        # pointer to point to current value node
        zero = zero_head
        one = one_head
        two = two_head

        # pointer for linked list
        curr = head
        while curr != None:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
        
        zero.next = one_head.next if one_head.next else two_head.next
        one.next = two_head.next
        two.next = None

        head = zero_head.next
        return head