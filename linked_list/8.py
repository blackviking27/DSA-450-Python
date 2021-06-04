# Add 1 to a number represented as linked list 

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Solution:
    def add_llist(self, head):
        def reverse(head):
            curr = head
            next = None
            prev = None
            while curr != None:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev
        
        # reversing the linked list
        head = reverse(head)

        curr = head
        while curr != None :
            if curr.next == None and curr.data == 9:
                curr.data = 1
                temp = Node(0)
                temp.next = head
                head = temp
                curr = curr.next
            
            elif curr.data == 9:
                curr.data = 0
                curr = curr.next
            else:
                curr.data += 1
                curr = curr.next
                break
        head = reverse(head)
        return head