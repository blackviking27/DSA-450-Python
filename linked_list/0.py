# Reverse a linked list

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # iterative method
    def reverse_itr(self): # passing the root node
        prev_node = None
        current_node = self.head
        next_node = None

        while current_node != None:
            next_node = current_node.next # next node pointer is pointing to the next node
            current_node.next = prev_node # current node's next pointer is pointing to the prev node
            prev_node = current_node # previous node pointer is now pointing to the current node
            current_node = next_node # current node pointer is now pointing to the next node
        
        self.head = prev_node # initialising new head

    # recursive method
    def reverse_recur(self):
        
        def _reverse_recur(curr, prev):
            if curr.next is None:
                # making it the head
                self.head = curr
                # pointing to the prev node
                curr.next = prev
                return
            
            next = curr.next # pointing to the next element
            curr.next = prev # poiting to the current which in the next recursive call becomes the prev element

            _reverse_recur(next, curr)

        if self.head is None:
            return
        _reverse_recur(self.head, None)




    # insert new value in the linked list at the beginning
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.data) + " "
            temp = temp.next
        print(result)

# creating the linked list object
ll = LinkedList()

# inserting the values into the linked list
ll.push(10)
ll.push(12)
ll.push(23)
ll.push(25)

# printing the result
print("Original Order")
ll.print()

print("Reversed Order")
ll.reverse_recur()
ll.print()