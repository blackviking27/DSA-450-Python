# Given a linked list of 0s, 1s and 2s, sort it. 
# Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. 
# The task is to segregate 0s, 1s, and 2s linked list such that all zeros 
# segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s

class Solution:
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
