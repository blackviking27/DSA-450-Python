# Merge Sort for Linked List 
# Given Pointer/Reference to the head of the linked list, 
# the task is to Sort the given linked list using Merge Sort.
# Note: If the length of linked list is odd, 
# then the extra node should go in the first list while splitting.

class Solution:

    def find_middle(curr):
        slow = curr
        fast = curr.next

        while fast != None:
            fast = fast.next
            if fast != None:
                slow = slow.next
                fast = fast.next

        return slow

    def merge(self, first, second):
        answer = None

        # If one of the linked list is empty
        if not first:
            return second
        elif not second:
            return first
        
        if first.data <= second.data:
            answer = first
            answer.next = self.merge(first.next, second)
        else:
            answer = second
            answer.next = self.merge(first, second.next)
        
        return answer

    def mergeSort(self, head):

        if not head or not head.next: return head
        
        # getting the middle element
        middle = self.find_middle(head)
        middleNext = middle.next
        middle.next = None

        # taking the left part of the linked list
        left = self.mergeSort(head)

        # taking the right  part of the linked list
        right = self.mergeSort(middleNext)

        # merging the left and right linked list
        head = self.merge(left, right)
        return head