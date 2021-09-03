# Interleave the first half of the queue with second half

from queue import Queue

def interleaveQueue(q):
    n = len(q.queue)
    if n % 2 != 0:
        print("Enter even number of items")
    
    stack = []
    # inserting the fist half elements into the stack
    mid = n // 2
    for i in range(mid):
        stack.append(q.get())

    # push the stack elements back into the stack
    while stack:
        q.put(stack.pop())
    
    # enqueue the second half elements back into the queue
    for i in range(mid):
        temp = q.get()
        q.put(temp)
    
    # push the first half in the stack again
    for i in range(mid):
        stack.append(q.get())
    
    # now interleave the elements
    while stack:
        q.put(stack.pop())
        temp = q.get()
        q.put(temp)
    
    print(q.queue)


# using the reverse stack function
def insertAtBottom(s, val):
    if len(s) == 0:
        s.append(val)
    else:
        top = s.pop()
        insertAtBottom(s, val)
        s.append(top)

def reverse(s):
    if s:
        curr = s.pop()
        reverse(s)
        insertAtBottom(s, curr)

def interleaveQueue_2(q):
    n = len(q.queue)
    stack = []

    for i in range(n // 2):
        stack.append(q.get())
    
    # reverse the stack
    reverse(stack)
    print(stack)

    # interleave the queue
    while stack:
        q.put(stack.pop())
        temp = q.get()
        q.put(temp)
    
    print(q.queue)

# driver code
q = Queue()
q.put(11) 
q.put(12) 
q.put(13) 
q.put(14)
q.put(15) 
q.put(16) 
q.put(17) 
q.put(18) 
q.put(19) 
q.put(20)

# Run either of the functions

# without using the stack reverse function
interleaveQueue(q)

# using the stack reverse function
interleaveQueue_2(q)