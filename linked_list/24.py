# Reverse a doubly linked list in groups of given size

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
    
    def reverse_by_k(self, head, k):
        
        if head == None:
            return None

        head.prev = None

        curr = head
        next = None # keeps track of the head of the new k linked list
        prev = None # keeps track of the new head of the reversed list

        count = 0
        while count < k and curr != None:
            prev = curr
            next = curr.next
            curr.next, curr.prev = curr.prev, curr.next
            curr = next
            count += 1
        
        if next != None:
            head.next = self.reverse_by_k(next, k)
            head.next.prev = head
        
        return prev
        
dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)
dll.push(45)
dll.push(24)
dll.printList()
dll.head = dll.reverse_by_k(dll.head,3)
dll.printList()