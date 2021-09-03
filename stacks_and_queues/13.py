# Reverse a stack using recursion

class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
    
    def isEmpty(self):
        return len(self.stack) == 0

    def pop(self):
        return self.stack.pop() if not self.isEmpty()  else -1
    
    def insertAtBottom(self, val):
        if self.isEmpty():
            self.push(val)
        else:
            top = self.pop()
            self.insertAtBottom(val)
            self.push(top)
    
    def reverseStack(self):
        if not self.isEmpty():
            curr = self.pop()
            self.reverseStack()
            self.insertAtBottom(curr)
    
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)

print(s.stack)
s.reverseStack()
print(s.stack)
