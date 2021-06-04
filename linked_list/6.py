# Remove duplicates from an unsorted linked list
class Solution:
    def removeDuplicates(self, head):

        if head is None:
            return head

        prev = head
        nodes = {head.data: 1}
        curr = head.next

        while curr != None:
            if curr.data in nodes:
                prev.next = curr.next
            else:
                nodes[curr.data] = 1
                prev = curr
            curr = curr.next
        
        return head