# Flattening a Linked List 
# Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
# (i) a next pointer to the next node,
# (ii) a bottom pointer to a linked list where this node is head.
# Each of the sub-linked-list is in sorted order.
# Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 

class Solution:
    def merge(self, h1, h2):
        if h1 == None:
            return h2
        if h2 == None:
            return h1
        
        res = None
        if h1.data < h2.data:
            res = h1
            res.bottom = self.merge(h1.bottom, h2)
        else:
            res = h2
            res.bottom = self.merge(h1, h2.bottom)

        res.next = None
        return res
    
    def flatten(self, root):
        if root == None or root.next == None:
            return root
        return self.merge(root, self.flatten(root.next))