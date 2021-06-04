# Sort a k sorted doubly linked list
# Given a doubly linked list containing n nodes, 
# where each node is at most k away from its target position in the list. 
# The problem is to sort the given doubly linked list.


# Getting the priority queue
from queue import PriorityQueue

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


    # sorting the doubly linked list
    def sort(self, head, k):
        if head == None:
            return None
        
        pq = PriorityQueue(k + 1)

        i = 0
        # inserting k elements into the priority queue
        while i <= k and head != None:
            # putting tuple as head.data and head object 
            # since we are comparing priority according to the data
            pq.put((head.data, head)) 
            head = head.next
            i += 1
        
        newHead = None
        curr = None # will point to the new head

        while not pq.empty():
            if newHead == None:
                newHead = pq.get()[1] # getting the top node
                newHead.prev = None
                curr = newHead
            else:
                temp = pq.get()[1] # getting the node at the top of pq
                curr.next = temp
                temp.prev = curr
                curr = curr.next
            
            if head != None:
                pq.put((head.data, head))
                head = head.next
        # the end node
        curr.next = None

        return newHead

dll = DoublyLinkedList()
dll.push(8)
dll.push(56)
dll.push(12)
dll.push(2)
dll.push(6)
dll.push(3)

print("Before sort")
dll.printList()

print("After sort")
dll.head = dll.sort(dll.head, 2)
dll.printList()