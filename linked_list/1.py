# Reverse a Linked List in groups of given size

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # function to reverse k elements at a time
    def reverse(self, head, k):

        if head == None:
            return None
        
        curr = head
        next = None
        prev = None
        count = 0 # to keep track of the k elements

        # reversing the k elements 
        while curr != None  and count < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        
        # now the head is at the last of the reversed list of k elememts, the next of head would
        # be the first node of the next k elements in reversed order
        # next node acts as the head of the current k elements and at the last element the next node would point to the head
        # of the next k elements and prev node would be the last element of the k elements. This prev node will
        # become the head.next for the previous k elements
        if next != None:
            head.next = self.reverse(next, k)
        
        return prev

    def printList(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.data) + " "
            temp = temp.next
        print(result)

llist = LinkedList()
llist.push(9)
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("Original List")
llist.printList()

k = 3
print("Reversed k elements list")
llist.head = llist.reverse(llist.head, k)
llist.printList()