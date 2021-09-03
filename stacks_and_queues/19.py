# Implement Stack using Queue

def push(x):
    
    # global declaration
    global queue_1
    global queue_2
    queue_2.append(x)
    for el in queue_1:
        queue_2.append(el)
    
    queue_1 = []
    queue_1, queue_2 = queue_2, queue_1


#Function to pop an element from stack using two queues.     
def pop():
    
    # global declaration
    global queue_1
    global queue_2
    return queue_1.pop(0) if queue_1 else -1

queue_1 = []
queue_2 = []