# Remove duplicates from a sorted linked list

class Solution:
    def remove(self, head):
        curr = head
        while curr.next != None:
            if curr.data == curr.next.data:
                curr.next = curr.next.next
            else:
                curr = curr.next
        