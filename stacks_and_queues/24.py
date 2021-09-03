# Implement a Circular queue

class CircularQueue:
    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None]*self.size
        self.rear = self.front = -1

    def Enqueue(self, x):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full\n")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = x
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = x
    
    def Dequeue(self):
        if self.front == -1:
            print("Queue is empty \n")
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    