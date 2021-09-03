# Implement Queue from Scratch

class Queue:
    def __init__(self, capacity) -> None:
        self.front =  self.size = 0
        self.rear = capacity - 1
        self.capacity = capacity
        self.queue = [None]*capacity

    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def EnQueue(self, val):
        if self.isFull():
            print("Queue is Full")
            return
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = val
        self.size += 1
        print(f"Insert {val} into the queue")
    
    def DeQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return
        print(f"Removed {self.queue[self.front]}")
        self.front =( self.front + 1 ) % self.capacity
        self.size -= 1
    
    def queue_front(self):
        print(f"Element at front {self.queue[self.front]}")
    
    def queue_rear(self):
        print(f"Element at end {self.queue[self.rear]}")

# Driver code
queue = Queue(30)
queue.EnQueue(10)
queue.EnQueue(20)
queue.EnQueue(30)
queue.EnQueue(40)
queue.DeQueue()
queue.queue_front()
queue.queue_rear()