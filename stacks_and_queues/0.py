# Implement Stack from Scratch

class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, val):
        # Inserted item is always at the end
        self.stack.append(val)
    
    def pop(self, val):
        # Removing the element from the end in the stack
        self.stack.pop()
    
    def printStack(self):
        print(f"Stack right now : {self.stack}")
    
    def peek(self):
        # Returns the  element at the top
        if self.stack:
            return self.stack[-1]
        else:
            return None
    
    def size(self):
        # Returns the size of the stack
        return len(self.stack) if self.stack else 0
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False