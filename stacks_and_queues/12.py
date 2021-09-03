# Implement a method to insert an element at its bottom without using any other data structure.

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop() 
        else:
            return -1
    
    def isEmpty(self):
        return len(self.stack) == 0

    def insertAtBottom(self, val):
        if self.isEmpty():
            self.push(val)
        else:
            # taking the top element
            top = self.pop()

            # inserting at the bottom
            self.insertAtBottom(val)

            # inserting the top element again
            self.push(top)
    
    def printStack(self):
        print(*self.stack)

s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.printStack()

s.insertAtBottom(40)
s.printStack()