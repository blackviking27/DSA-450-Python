# Count triplets in a sorted doubly linked list whose sum is equal to a given value x

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

    def count_pairs(self, first, last, k):
        count = 0
        while first != last and last.prev != first and first != None and last != None:
            if first.data + last.data == k:
                count += 1
                first = first.next
                last = last.prev
            elif first.data + last.data < k:
                first = first.next
            else:
                last = last.prev
        return count

    def count_triplets(self, x):
        if self.head == None:
            return 0
        
        current, first, last = self.head, None, self.head
        count = 0
        while last.next != None:
            last = last.next
        
        while current != None:
            first = current.next

            # utilizing the function which returns sum equal to diff of current node data and target
            count += self.count_pairs(first, last, x - current.data)
            current = current.next
        
        return count

dll = DoublyLinkedList()
dll.push(9)
dll.push(8)
dll.push(6)
dll.push(5)
dll.push(4)
dll.push(5)
dll.push(1)

dll.printList()
print(dll.count_triplets(17))