# Rotate Doubly linked list by N nodes

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None        

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        
        temp = Node(data)

        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def printList(self):
        temp = self.head
        res = ""
        while temp != None:
            res += str(temp.data) + " "
            temp = temp.next
        print(res)
    
    def rotate(self, n):
        newHead = self.head
        prev = None
        for i in range(n):
            prev = newHead
            newHead = newHead.next #  pointing to the n + 1th node
        
        prev.next = None # prev is end node of the first n nodes
        newHead.prev = None # cutting ties with the first n nodes
        curr = newHead

        while curr.next != None:
            curr = curr.next

        curr.next = self.head
        self.head.prev = curr

        self.head = newHead

dll = DoublyLinkedList()
dll.push('e')
dll.push('d')
dll.push('c')
dll.push('b')
dll.push('a')

print("Before rotating")
dll.printList()

dll.rotate(2)
print("After rotating")
dll.printList()
