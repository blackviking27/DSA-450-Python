# Intersection Point in Y Shapped Linked Lists
# Given two singly linked lists of size N and M, 
# write a program to get the point where two linked lists intersect each other

class Solution:
    def intersect(self, head1, head2):
        ptr1 = head1
        ptr2 = head2

        c1, c2 = 0, 0

        # calculating the length of first linked list
        while ptr1:
            c1 += 1
            ptr1 = ptr1.next
        
        # calculating the length of second linked list
        while ptr2:
            c2 += 1
            ptr2 = ptr2.next
        
        # initialising the heads again
        ptr1 = head1
        ptr2 = head2

        diff = abs(c1 - c2)

        # bringing the lists to the same level
        if c1 > c2:
            for i in range(diff):
                ptr1 = ptr1.next
        elif c2 > c1:
            for i in range(diff):
                ptr2 = ptr2.next
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        
        if ptr1: return ptr1.data
        return -1
