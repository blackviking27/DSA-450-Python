# Implement Queue using Stack 

class Queue:
    def __init__(self) -> None:
        self.s1 = []
        self.s2 = []
    
    def Enqueue(self, x):
        while len(self.s1) != 0:
            self.s2.append(self.s1.pop())
        
        self.s1.append(x)

        while len(self.s2) != 0:
            self.s1.append(self.s2.pop())
    
    def Dequeue(self):
        return self.s1.pop() if self.s1 else -1
