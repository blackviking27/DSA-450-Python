# Design a stack with operations on middle element

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = self.next = None
    
class Stack:
    def __init__(self):
        self.mid = None
        self.head = None
        self.count = 0

def push(ms, val):
    # creatinga new node
    node = Node(val)

    # poiting to the head since we are inserting the node at the head
    node.next = ms.head

    # increasing the number of elements in the stack
    ms.count += 1
    if ms.count == 1:
        # if only one node is present
        ms.mid = node
    else:
        # poiting prev to new node at the start
        ms.head.prev = node
        if ms.count % 2 != 0:
            ms.mid = ms.mid.prev

    ms.head = node

def pop(ms):
    if ms.count == 0:
        return -1

    head = ms.head
    ms.head = ms.head.next

    if ms.head != None:
        ms.head.prev = None
    
    ms.count -= 1

    if ms.count % 2 == 0:
       ms.mid = ms.mid.next

    return head.data

def getMiddle(ms):
    if ms.count == 0:
        return -1
    return ms.mid.data

def printStack(ms):
    curr = ms.head
    while curr != None:
        print(f"{curr.data} <--> ", end =" ")
        curr = curr.next

# driver code

ms = Stack()
push(ms, 11)
push(ms, 22)
push(ms, 33)
push(ms, 44)
push(ms, 55)
push(ms, 66)
push(ms, 77)

printStack(ms)

print()
print(pop(ms))
print(pop(ms))
print(pop(ms))

printStack(ms)
