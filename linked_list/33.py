# Segregate even and odd nodes in a Link List

class node:
    def __init__(self) -> None:
        self.data = None
        self.next = None

class Solution:
    def divide(self, N, head):
        
        even = None
        odd = None
        e = None
        o = None
        
        while head != None:
            if head.data % 2 == 0:
                if even == None:
                    even = head
                    e = even
                else:
                    e.next = head
                    e = e.next
            else:
                if odd == None:
                    odd = head
                    o = odd
                else:
                    o.next = head
                    o = o .next
            head = head.next
        
        if e: e.next = None # if there are any even terms
        if o: o.next = None # pointing the last node of odd
        if even: return even 
        return odd