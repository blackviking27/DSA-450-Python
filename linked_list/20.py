# Find pairs with given sum in doubly linked list


class Node:
    def __init__(self, data):
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

    # function gives back the pair
    def pairsum(self, k):
        res = []

        first = self.head # points at he beginning
        second = self.head # points at he end
        while second.next != None:
            second = second.next
        # run a loop till first and second are not equal (first != second)
        # or first and second after just crossing each other ( second.next != first )
        while first != second and second.next != first:
            if first.data + second.data == k:
                res.append([first.data, second.data])
                first = first.next
                second = second.prev
            
            elif first.data + second.data < k:
                first = first.next
            else:
                second = second.prev
        
        return res if len(res) > 0 else -1
    
dll = DoublyLinkedList()
dll.push(9)
dll.push(8)
dll.push(6)
dll.push(5)
dll.push(4)
dll.push(2)
dll.push(1)

dll.printList()

print(dll.pairsum(7))
